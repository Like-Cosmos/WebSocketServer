node{
    stage('Prepare') {
        echo "1.Fetch branch code to update dependency packages"
        sh "cd WebSocketServer"
        sh "pip3 install -r requirements.txt"
        sh "git pull"


    }

    stage('Deploy') {
        echo "2. Deploy Stage"
        if (env.BRANCH_NAME == 'master') {
            input "确认要部署线上环境吗？"
        }

    }

}


