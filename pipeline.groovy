pipeline {
    agent { label 'host-agent' }
    environment {
        PYTHON_VERSION = "3.11"
        FLASK_ENV = "developement"
        FLASK_APP = "src/app.py"
    }
    stages {
        stage('Check if python exists') {
            steps {
                sh 'python3.11 --version'
                sh 'docker ps'
            }
        }
    }
}