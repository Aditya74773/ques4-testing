pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Check Python') {
            steps {
                bat '''
                    echo Checking Python installation...
                    "C:\\Users\\Aditya kumar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version
                    "C:\\Users\\Aditya kumar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    echo Installing Python dependencies...
                    "C:\\Users\\Aditya kumar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Test Suite') {
            steps {
                bat '''
                    echo Running Q4 test suite...
                    "C:\\Users\\Aditya kumar\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v --junitxml=junit.xml --html=report.html --self-contained-html
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'junit.xml'

                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Q4 Test Report'
                ])
            }
        }
    }

    post {
        success {
            echo 'Q4 Test Suite completed successfully'
        }

        failure {
            echo 'Q4 Test Suite failed'
        }
    }
}