pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "muhammedelshafei/flask-devops-app"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                pip install -r requirements.txt --break-system-packages
                pytest test_app.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Pushing to Docker Hub and deploying...'
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker compose up -d"
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            sh 'docker logout'
        }
    }
}