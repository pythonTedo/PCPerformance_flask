pipeline {
    agent any
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