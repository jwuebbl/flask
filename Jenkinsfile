pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Pulling the latest archived successful lolKda build files.'
                copyArtifacts(projectName: 'lolKda', filter: 'lolKda.html', selector: lastSuccessful(), target: 'app/templates/')
                copyArtifacts(projectName: 'lolKda', filter: 'lolKdaRunTime.js', selector: lastSuccessful(), target: 'app/static/js/')
                copyArtifacts(projectName: 'lolKda', filter: 'lolKdaPolyfills.js', selector: lastSuccessful(), target: 'app/static/js/')
                copyArtifacts(projectName: 'lolKda', filter: 'lolKdaMain.js', selector: lastSuccessful(), target: 'app/static/js/')
                copyArtifacts(projectName: 'lolKda', filter: 'lolKdaStyles.js', selector: lastSuccessful(), target: 'app/static/styles/')

                sh 'docker build -t jwuebblz/flask:latest .'
            }
        }
    }
}
