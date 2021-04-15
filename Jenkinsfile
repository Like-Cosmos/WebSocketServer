node{
    stage('Prepare') {
        echo "1.Prepare Stage"
        script {
            sh "cd WebSocketServer"
            build_tag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            if (env.BRANCH_NAME != 'master') {
                build_tag = "${env.BRANCH_NAME}-${build_tag}"
            }
        }

    }
    stage('Build') {
        echo "2.Fetch branch code to update dependency packages"
        sh "cd WebSocketServer"
        sh "git pull"
    }
    stage('Deploy') {
        echo "3. Deploy Stage"
        if (env.BRANCH_NAME == 'master') {
            input "确认要部署线上环境吗？"
        }

    }

}


