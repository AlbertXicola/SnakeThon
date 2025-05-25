pipeline {
    agent any

    parameters {
        string(name: 'GIT_URL', defaultValue: '', description: 'URL del repositorio Git')
    }

    environment {
        SONARQUBE_SERVER = 'SonarQube'
        SONAR_AUTH_TOKEN = credentials('sonarqube-token')
        PATH = "/opt/sonar-scanner/bin:${env.PATH}" 
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    if (!params.GIT_URL) {
                        error("No se proporcionó URL de Git para checkout.")
                    }
                    git url: params.GIT_URL, branch: 'main'
                }
            }
        }
        // Resto de stages sin cambios
    }
}
