#!/usr/bin/env groovy

pipeline {
  agent any
  // triggers {
  //   pollSCM('H/5 * * * *')
  // }

  stages {
    stage('Checkout'){
      checkout scm
    }
    stage('Build') {
      steps {
        dir 'django'
        app = docker.build('taskmngr1:5000/taskmngr')
        app.push()
      }
    }
    // stage('Test') {
    //   steps {
        // sh 'python django/manage.py test'
    //   }
    // }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}
