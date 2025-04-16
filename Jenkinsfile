pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning GitHub repo to Jenkins'){
            steps{
                script {
                    echo 'Cloning GitHub repo to Jenkins................'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git']])


                }
            }
        }
    stage('Setting Up Virtual Environment and installing dependencies'){
        steps{
            script{
                echo 'Setting Up Virtual Environment and installing dependencies'
                sh '''
                python -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -e .

                '''
            }
        }
    }
}
