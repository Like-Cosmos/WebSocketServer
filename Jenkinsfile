#!groovy

String workspace = "/home/dension/job"

pipeline{
    agent {
        node{
            label "master"
            customWorkspace "${workspace}"
        }
    }
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
    }
    stages {
        stage('拉代码'){
            steps{
                echo '拉代码'
                sh 'git clone git@github.com:Like-Cosmos/WebSocketServer.git';
            }
        }
    }
}