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
                    sh '''
                        bash -c "
                        python3.11 -m venv ${SRC_DIR}/venv
                        source ${SRC_DIR}/venv/bin/activate
                        pip install -r requirements.txt
                        "
                        '''
                }
            }
        }
        stage('Run tests') {
            steps {
                sh 'make test'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up workspace'
            cleanWS()
            
        }
    }
}