node {
    stage('build-using-scm'){
     echo '加载环境';
        sh 'cd /home/job'
        sh 'git clone https://github.com/Like-Cosmos/WebSocketServer.git';
        sh 'pip3 install -r WebSocketServer/requirements.txt';
    }
    
    stage('test-using-scm'){
     echo 'test';
    }
    
    stage('deploy-using-scm'){
     echo 'run';
        sh 'python3 /home/job/WebSocketServer/WebSocketServer/socketTool.py'
    }
}
