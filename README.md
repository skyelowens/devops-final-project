# Automated CI/CD Pipeline with Security Scanning and Chat Notifications

## Project Overview

For this final DevOps project, we wanted to build something that feels like a realistic workflow instead of a one-off demo. Our idea is an automated CI/CD pipeline for a small Python Flask web application. In a manual setup, someone has to pull the latest code, run tests locally, build a Docker image, log in to a server, restart the container, and then ping the team in chat to say the new version is live. That process gets repetitive, and it is easy to miss steps or forget what was done last time.

Our goal was to wire those pieces together so that, from a developer’s point of view, the main action is just pushing code to the `main` branch. Once the code is pushed, the Jenkins pipeline takes over and handles testing, building, scanning, pushing the image, deploying the container, and notifying the team in Webex.

## Technologies Used

- **Python / Flask** – simple web app with a health check route  
- **Pytest** – unit tests to verify the app responds correctly  
- **GitHub** – source control and webhook trigger for Jenkins  
- **Jenkins** – CI/CD pipeline engine  
- **Docker** – container image build and runtime for the app  
- **Trivy** – container image security scanner (new tool for this project)  
- **Docker Hub** – remote registry for versioned images  
- **Webex Bot + Webex REST API** – chat notifications for pipeline results  

## How the Workflow Works

1. We make a code change in the Flask app, commit it, and push to the `main` branch on GitHub.  
2. GitHub sends a webhook to Jenkins, which automatically starts the `devops-final-ci-cd` pipeline.  
3. Jenkins checks out the latest code, installs dependencies, and runs the test suite with `pytest`.  
4. If the tests pass, Jenkins builds a Docker image for the app and tags it with the Jenkins build number.  
5. Trivy scans the freshly built image for known vulnerabilities and fails the pipeline if any **CRITICAL** issues are found.  
6. If the scan is clean, Jenkins logs in to Docker Hub and pushes the tagged image to the `skyelowens/devops-demo` repository.  
7. Jenkins then deploys the new container, stopping any old container and starting a new one on port `5000`.  
8. At the end of the pipeline, a Webex bot posts a message in our Webex space with the build result (success or failure) and the build number.  

This turns one `git push` into a full automated build, test, security scan, deploy, and notify workflow.

## Repository Layout

```text
devops-final-project/
├── app/
│   ├── app.py              # Flask app with / and /health routes
│   └── requirements.txt    # Python dependencies (Flask, pytest, requests)
├── tests/
│   └── test_app.py         # Pytest test for the /health route
├── scripts/
│   └── notify_webex.py     # Helper script that posts messages via Webex API
├── Dockerfile              # Builds the Flask app image
├── Jenkinsfile             # Jenkins pipeline definition
└── README.md               # Project overview and setup notes
