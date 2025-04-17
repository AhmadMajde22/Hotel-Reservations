pipeline{
    agents any
    stages{
        stage('Cloning GitHub repo to jenkins'){
            steps {
                echo 'Cloning GitHub repo to jenkins..................'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github-token', url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git']])
            }
        }
    }
}
