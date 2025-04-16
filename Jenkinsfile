pipeline{
    agent any

    stges{
        stage('Cloning GitHub repo to Jenkins'){
            steps{
                script {
                    echo 'Cloning GitHub repo to Jenkins................'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git']])


                }
            }
        }
    }
}
