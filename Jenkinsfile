#!/usr/bin/env groovy

pipeline {
  agent any
  // triggers {
  //   pollSCM('H/5 * * * *')
  // }

  stages {
    stage('Test') {
      steps {
        sh 'python django/manage.py test'
      }
    }
    stage('Build') {
      steps {
        echo 'Building..'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}
