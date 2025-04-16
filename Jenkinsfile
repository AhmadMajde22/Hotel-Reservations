pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GHCR_USER = 'AhmadMajde22'  // GitHub username
        GHCR_TOKEN = credentials('ghcr-token')  // GitHub token for authentication
        GHCR_REPO = "ghcr.io/${GHCR_USER}/ml-project"  // GHCR repository path
    }

    stages {
        stage('Cloning GitHub Repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins............'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/data-guru0/MLOPS-COURSE-PROJECT-1.git'
                        ]]
                    )
                }
            }
        }

        stage('Setting up Virtual Environment and Installing Dependencies') {
            steps {
                script {
                    echo 'Setting up Virtual Environment and Installing Dependencies............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image............'
                    sh '''
                    # Build the Docker image
                    docker build -t ${GHCR_REPO}:latest .
                    '''
                }
            }
        }

        stage('Login to GitHub Container Registry') {
            steps {
                withCredentials([string(credentialsId: 'ghcr-token', variable: 'GHCR_TOKEN')]) {
                    script {
                        echo 'Logging in to GHCR............'
                        sh '''
                        # Log in to GHCR using the token
                        echo ${GHCR_TOKEN} | docker login ghcr.io -u ${GHCR_USER} --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Pushing Docker Image to GHCR') {
            steps {
                script {
                    echo 'Pushing Docker Image to GHCR............'
                    sh '''
                    # Push the Docker image to GHCR
                    docker push ${GHCR_REPO}:latest
                    '''
                }
            }
        }
    }
}
