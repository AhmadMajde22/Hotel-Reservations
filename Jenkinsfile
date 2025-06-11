pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'ahmadmajde22/hotel-reservation-app'
        DOCKER_TAG = 'latest'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials' // Define Jenkins credentials
    }
    stages {
        stage('Cloning GitHub repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git']]
                    )
                }
            }
        }

        stage('Creating Virtual Environment') {
            steps {
                script {
                    echo 'Creating Virtual Environment...'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    '''
                }
            }
        }

        stage('Login to Docker Hub') {
    steps {
        script {
            echo 'Logging into Docker Hub...'
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                sh '''
                    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                '''
            }
        }
    }
}

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Docker Image to Docker Hub...'
                    sh '''
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
    }
}
