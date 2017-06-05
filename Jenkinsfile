#!/usr/bin/env groovy

pipeline {
  agent any
  // triggers {
  //   pollSCM('H/5 * * * *')
  // }

  stages {
    stage('Build') {
      steps {
        cd "django"
        sh "docker build ."
      }
    }
    stage('Test') {
      steps {
        // sh 'python django/manage.py test'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}
