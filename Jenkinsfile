pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins already checks out with "Pipeline script from SCM",
                // but we keep this for clarity and consistency.
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
    }
}
