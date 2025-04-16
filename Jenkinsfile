pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'ghcr.io/ahmadmajde22/jenkins-dind'  // Change this to your desired image name
        DOCKER_TAG = 'latest'  // You can replace with a dynamic tag if needed
        GHCR_TOKEN = credentials('ghcr-token')  // GitHub token (add this credential to Jenkins)
    }

    stages {
        stage('Cloning GitHub repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins................'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git'
                        ]])
                }
            }
        }

        stage('Setting Up Virtual Environment and installing dependencies') {
            steps {
                script {
                    echo 'Setting Up Virtual Environment and installing dependencies...'
                }

                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python -m pip install --upgrade pip
                    pip install -e .
                '''
            }
        }

        stage('Building Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'

                    // Build the Docker image
                    sh '''
                        docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    '''
                }
            }
        }

        stage('Login to GitHub Container Registry') {
            steps {
                script {
                    echo 'Logging in to GitHub Container Registry...'

                    // Docker login to GHCR
                    sh '''
                        echo ${GHCR_TOKEN} | docker login ghcr.io -u <your-github-username> --password-stdin
                    '''
                }
            }
        }

        stage('Pushing Docker Image to GHCR') {
            steps {
                script {
                    echo 'Pushing Docker image to GHCR...'

                    // Push the Docker image to GHCR
                    sh '''
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
    }
}
