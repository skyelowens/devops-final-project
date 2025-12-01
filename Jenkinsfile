pipeline {
    agent any

    environment {
        DOCKER_IMAGE    = "skyelowens/devops-demo"
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        WEBEX_TOKEN     = credentials('webex-token')
        WEBEX_ROOM_ID   = credentials('webex-room-id')
    }

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
                sh """
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                sh """
                    docker run --rm \
                      -v /var/run/docker.sock:/var/run/docker.sock \
                      aquasec/trivy:latest image \
                      --exit-code 1 --severity CRITICAL \
                      ${DOCKER_IMAGE}:${BUILD_NUMBER}
                """
            }
        }

        stage('Push Image') {
            steps {
                sh """
                    echo ${DOCKERHUB_CREDS_PSW} | docker login -u ${DOCKERHUB_CREDS_USR} --password-stdin
                    docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    docker pull ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker stop devops-demo || true
                    docker rm devops-demo || true
                    docker run -d --name devops-demo -p 5000:5000 ${DOCKER_IMAGE}:${BUILD_NUMBER}
                """
            }
        }
    }

    post {
        success {
            sh """
                WEBEX_TOKEN=${WEBEX_TOKEN} WEBEX_ROOM_ID=${WEBEX_ROOM_ID} \
                python3 scripts/notify_webex.py success ${BUILD_NUMBER}
            """
        }
        failure {
            sh """
                WEBEX_TOKEN=${WEBEX_TOKEN} WEBEX_ROOM_ID=${WEBEX_ROOM_ID} \
                python3 scripts/notify_webex.py failure ${BUILD_NUMBER} || true
            """
        }
    }
}

