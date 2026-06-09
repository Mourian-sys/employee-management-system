from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Alice", "department": "HR"},
    {"id": 3, "name": "David", "department": "Finance"}
]

@app.route('/')
def home():
    return "Employee Management System Running"

@app.route('/employees')
def get_employees():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
