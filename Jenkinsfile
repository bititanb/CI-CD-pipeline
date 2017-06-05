#!/usr/bin/env groovy

node {
  stage('Checkout'){
    checkout scm
  }
  stage('Build') {
    dir 'django'
    app = docker.build('taskmngr1:5000/taskmngr')
    app.push()
  }
  // stage('Test') {
  //   steps {
      // sh 'python django/manage.py test'
  //   }
  // }
  stage('Deploy') {
    echo 'Deploying....'
  }
}
