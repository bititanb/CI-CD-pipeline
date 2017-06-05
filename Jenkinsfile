#!/usr/bin/env groovy

pipeline {
  agent any
  // triggers {
  //   pollSCM('H/5 * * * *')
  // }

  stages {
    stage('Checkout'){
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        dir 'django'
        docker.build('taskmngr1:5000/taskmngr').push()
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
