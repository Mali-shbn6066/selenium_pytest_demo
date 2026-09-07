pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:/Users/malih/AppData/Local/Programs/Python/Python314/python.exe" -m pip install --upgrade pip'
                bat '"C:/Users/malih/AppData/Local/Programs/Python/Python314/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:/Users/malih/AppData/Local/Programs/Python/Python314/python.exe" -m pytest --alluredir=report --junitxml=test-results.xml --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }
}