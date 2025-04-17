pipeline {
    agent any
    environment {
        VENV_DIR ='venv'
    }
    stages {
        stage('Cloning GitHub repo to jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'jenkins-github-token', url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git']]
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
    }
}
