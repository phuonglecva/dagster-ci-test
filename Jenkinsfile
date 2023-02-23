
pipeline {
    agent any

    stages {
        stage('Build docker image') {
            steps {
                echo 'Building...'
                sh 'make build'
            }
        }
        stage('test helm version') {
            steps {
                    withKubeConfig([credentialsId: 'test', serverUrl: 'https://127.0.0.1:33975']) {
                            sh 'helm upgrade --install dagster dagster/dagster -f values.yaml'
                        }
            }
            }
        }
}

