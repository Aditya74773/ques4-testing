pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                    echo Installing Python dependencies...
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Test Suite') {
            steps {
                bat '''
                    echo Running Q4 test suite...
                    pytest -v --junitxml=junit.xml --html=report.html --self-contained-html
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