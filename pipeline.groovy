pipeline {
    agent { label 'host-agent' }
    environment {
        FLASK_ENV = "developement"
        FLASK_APP = "src/app.py"
        SRC_DIR = "src"
    }
    stages {
        stage('Check if python exists and docker exists') {
            steps {
                sh 'python3.11 --version'
            }
        }
        stage('Prepare venv') {
            steps {
                script {
                    sh 'python3.11 -m venv ${SRC_DIR}/venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run tests') {
            steps {
                sh 'make test'
            }
        }
        stage('Clean environment') {
            steps {
                sh 'deactivate; rm -rf ${SRC_DIR}/venv'
            }
        }
    }
}