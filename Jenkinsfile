pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                    pip3 install --break-system-packages --no-cache-dir -r app/requirements.txt
                    PYTHONPATH=. python3 -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t devops-demo:${BUILD_NUMBER} .
                '''
            }
        }
    }
}
