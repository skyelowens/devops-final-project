pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins will already have checked out the repo because we're using "Pipeline script from SCM",
                // but we'll leave this here for clarity.
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                    pip3 install --no-cache-dir -r app/requirements.txt
                    PYTHONPATH=. pytest
                '''
            }
        }
    }
}
