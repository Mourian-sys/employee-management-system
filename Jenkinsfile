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
                sh 'pip3 install -r backend/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'cd backend && pytest tests'
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
}
