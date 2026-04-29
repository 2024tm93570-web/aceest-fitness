pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = credentials('dockerhub-username')
        DOCKERHUB_TOKEN    = credentials('dockerhub-token')
        IMAGE_NAME         = 'acest-fitness'
        PYTHON             = '"C:\\Users\\amrut\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe"'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat "%PYTHON% -m pip install --upgrade pip"
                bat "%PYTHON% -m pip install -r requirements.txt"
            }
        }

        stage('Lint') {
            steps {
                echo 'Running Flake8 lint check...'
                bat "%PYTHON% -m pip install flake8"
                bat "%PYTHON% -m flake8 . || exit 0"
            }
        }

        stage('Test') {
            steps {
                echo 'Running Pytest...'
                bat "%PYTHON% -m pytest"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t aceest-gym-app .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                bat """
                    docker login -u %DOCKERHUB_USERNAME% -p %DOCKERHUB_TOKEN%
                    docker tag aceest-gym-app %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
                    docker push %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
                """
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}