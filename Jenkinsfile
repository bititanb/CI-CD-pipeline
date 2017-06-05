#!/usr/bin/env groovy

node {
  stage('Checkout'){
    git(url: 'https://bitbucket.org/bititanb/taskmngr')
  }
  stage('Build') {
    docker.withRegistry('https://taskmngr1:5000/') {
      dir 'django' {
        echo "$PWD"
        pwd
      }
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
