pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins already checks out the code, but we keep this for clarity
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                    pip3 install --break-system-packages --no-cache-dir -r app/requirements.txt
                    PYTHONPATH=. pytest
                '''
            }
        }
    }
}
