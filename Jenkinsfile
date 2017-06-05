#!/usr/bin/env groovy

node {
  stage('Checkout'){
    checkout scm
  }
  stage('Build') {
    dir 'django'
    def app = docker.build('taskmngr1:5000/taskmngr')
    app.push()
  }
  stage('Deploy') {
    echo 'Deploying....'
  }
}
