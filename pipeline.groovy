pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }
    environment {
        PYTHON_VERSION = "3.11"
        FLASK_ENV = "developement"
        FLASK_APP = "src/app.py"
    }
    stages {
        stage('Check if python exists') {
            steps {
                sh 'python3.11 --version'
            }
        }

    }
}