pipeline {
    agent { 
        dockerfile {
            filename 'Dockerfile.sast'
            args '--user=$(id -u):$(id -g) --volume=$(pwd):/code:Z'
        } 
    }

    environment {
        CODE_DIR="/code"
    }

    stages {
        stage('Run Snyk SAST inside Docker Container') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'snyk_client_credentials',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {
                    // sh 'echo "~~~~~~~~~~~~~~"'
                    sh '''
                    pwd
                    ls -latr
                    whoami

                    '''
                }
            }
        }
    }

    // post {
    //     always {
    //         // Safely list the output directory from inside the Docker volume
    //         dir('/srv/jekyll') {
    //             sh 'ls -ltr'
    //         }
    //     }
    // }
}
