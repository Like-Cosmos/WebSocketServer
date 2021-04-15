node {
    stage('build-using-scm'){
     echo '加载环境';
        sh 'ls';
        sh 'pip3 install -r requirements.txt';
    }
    
    stage('test-using-scm'){
     echo 'test';
    }
    
    stage('deploy-using-scm'){
     echo 'run';
        sh 'python3 ～/WebSocketServer/socketTool.py'
    }
}
