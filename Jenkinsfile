pipeline {
    agent any
    stages {
        stage('Build the flask docker image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCreds') {
                        def image = docker.build('jwuebblz/flask:latest')
                        image.push()
                    }
                }
            }
        }
    }
}
