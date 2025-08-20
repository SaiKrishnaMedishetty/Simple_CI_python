pipeline {
  agent any

  triggers {
    githubPush()
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Install deps') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          . .venv/bin/activate
          export PYTHONPATH=$PWD
          mkdir -p reports
          pytest --junitxml=reports/junit.xml \
                 --html=reports/report.html --self-contained-html
        '''
      }
    }
  }

  post {
    always {
      junit 'reports/junit.xml'
      archiveArtifacts artifacts: 'reports/*'
      publishHTML(target: [
        reportDir: 'reports',
        reportFiles: 'report.html',
        reportName: 'Pytest HTML Report',
        keepAll: true
      ])
      cleanWs()
    }
  }
}
