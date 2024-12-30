pipeline {
    agent any
    environment {
        PYTHON_VERSION = "3.11"
        FLASK_ENV = "developement"
        FLASK_APP = "src/app.py"
    }
    stages {
        stage('Check if python exists') {
            steps {
                script {

                    def pythonInstalled = sh(script: "python --version", returnStatus: true)
                    if (pythonInstalled != 0) {
                        echo "Python is not installed"
                        currentBuild.result = 'FAILURE'
                        error("Python is not installed")
                    }
                }
            }
        }

    }
}