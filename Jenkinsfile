pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'ghcr.io/ahmadmajde22/jenkins-dind'
        DOCKER_TAG = 'latest'
        GHCR_TOKEN = credentials('ghcr-token')  // Must be stored in Jenkins Credentials
        GITHUB_USERNAME = 'ahmadmajde22'
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
                            url: 'https://github.com/ahmadmajde22/Hotel-Reservations.git'
                        ]]
                    )
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
                        pip install pytest pytest-cov pytest-mock
                        [ -f requirements.txt ] && pip install -r requirements.txt || true
                        pip install -e .
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
                        echo "Tests directory contents:"
                        ls -la tests/ || echo "tests directory not found"
                        pytest tests/ -v
                    '''
                }
            }
        }

        stage('Building Docker Image') {
            steps {
                script {
                    echo 'Building Docker image'
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Login to GitHub Container Registry') {
            steps {
                script {
                    echo 'Logging in to GitHub Container Registry'
                    sh """
                        echo "${GHCR_TOKEN}" | docker login ghcr.io -u "${GITHUB_USERNAME}" --password-stdin
                    """
                }
            }
        }

        stage('Pushing Docker Image to GHCR') {
            steps {
                script {
                    echo 'Pushing Docker image to GHCR'
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
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
