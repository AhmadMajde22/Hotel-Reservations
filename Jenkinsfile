pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'ghcr.io/Ahmadmajde22/jenkins-dind'
        DOCKER_TAG = 'latest'
        GHCR_TOKEN = credentials('ghcr-token')
        GITHUB_USERNAME = 'Ahmadmajde22'  // Replace with your GitHub username
    }

    stages {
        stage('Cloning GitHub repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins'
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

        stage('Setting Up Virtual Environment') {
    steps {
        script {
            echo 'Setting Up Virtual Environment and installing dependencies'
            sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                python -m pip install --upgrade pip
                pip install pytest pytest-cov pytest-mock  # Install test dependencies
                pip install -r requirements.txt || true   # Install project dependencies if requirements.txt exists
                pip install -e .                         # Install package in editable mode
            '''
        }
    }
}

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests'
                    sh '''
                        . ${VENV_DIR}/bin/activate
                        python -m pytest tests/
                    '''
                }
            }
        }

        stage('Building Docker Image') {
            steps {
                script {
                    echo 'Building Docker image'
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }

        stage('Login to GitHub Container Registry') {
            steps {
                script {
                    echo 'Logging in to GitHub Container Registry'
                    sh 'echo ${GHCR_TOKEN} | docker login ghcr.io -u ${GITHUB_USERNAME} --password-stdin'
                }
            }
        }

        stage('Pushing Docker Image to GHCR') {
            steps {
                script {
                    echo 'Pushing Docker image to GHCR'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Cleaning up...'
        }
        failure {
            echo 'Pipeline failed! Check the logs for details'
        }
        always {
            script {
                echo 'Cleaning up workspace'
                sh '''
                    docker logout ghcr.io
                    rm -rf ${VENV_DIR}
                '''
                cleanWs()
            }
        }
    }
}
