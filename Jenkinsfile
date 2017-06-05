#!/usr/bin/env groovy

node {
  stage('Checkout'){
    checkout scm
  }
  stage('Build') {
    docker.withRegistry('https://taskmngr1:5000/') {
      echo '$PWD'
      // dir 'django' {
      //   docker.build('taskmngr').push('latest')
      // }
    }
    // dir 'django'
    // def app = docker.build('taskmngr1:5000/taskmngr')
    // app.push()
  }
  stage('Deploy') {
    echo 'Deploying....'
  }
}
