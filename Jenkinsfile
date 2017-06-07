#!/usr/bin/env groovy

node {
  stage('Checkout'){
    git(url: 'https://bitbucket.org/bititanb/taskmngr')
  }
  stage('Build') {
    gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
    // short SHA, possibly better for chat notifications, etc.
    shortCommit = gitCommit.take(6)
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
