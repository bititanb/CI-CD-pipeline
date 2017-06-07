#!/usr/bin/env groovy

node {
  stage('Checkout'){
    git(url: 'https://bitbucket.org/bititanb/taskmngr')
  }
  stage('Build') {
    echo $GIT_COMMIT
    // docker.withRegistry('https://taskmngr1:5000/') {
      // dir('django') {
      //   docker.build('taskmngr').push()
      // }
    // }
  }
  stage('Deploy') {
    echo 'Deploying....'
  }
}
