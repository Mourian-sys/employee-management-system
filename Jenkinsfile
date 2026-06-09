pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user -r backend/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'cd backend && python3 -m pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop employee-app || true
                docker rm employee-app || true

                docker run -d \
                --name employee-app \
                -p 5000:5000 \
                employee-app
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful'
        }

        failure {
            echo 'Deployment Failed'
        }
    }
}
