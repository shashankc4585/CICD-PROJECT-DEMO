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
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest'
            }
        }
    }

    post {
        success {
            echo '5G RAN CI Pipeline PASSED'
        }

        failure {
            echo '5G RAN CI Pipeline FAILED'
        }
    }
}