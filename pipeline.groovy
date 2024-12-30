pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }
    environment {
        FLASK_ENV = "developement"
        FLASK_APP = "src/app.py"
    }
    stages {
        stage('Check if python exists') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }

    }
}