pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Pulling the latest archived successful lolKda build files.'
                copyArtifacts(projectName: 'lolKda', filter: 'dist/lol-kda/lolKda.html', selector: lastSuccessful(), target: 'app/templates/')
                copyArtifacts(projectName: 'lolKda', filter: 'dist/lol-kda/*.js', selector: lastSuccessful(), target: 'app/static/js/')
                copyArtifacts(projectName: 'lolKda', filter: 'dist/lol-kda/*.css', selector: lastSuccessful(), target: 'app/static/styles/')

                sh 'docker build -t jwuebblz/flask:latest ./app'
            }
        }
    }
}
