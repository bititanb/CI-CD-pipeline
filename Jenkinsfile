#!/usr/bin/env groovy

node {
  stage('Checkout'){
    ansiblePlaybook(
        playbook: "/etc/ansible/taskmngr.yaml",
        tags: 'taskmngr-kubernetes',
        extraVars: [
          app_checkout: "true",
          app_build: "true",
          app_deploy_testing: "true",
          app_test: "true",
          app_deploy_prod: "true",
        ]
    )
  }
  stage('Build') {
    echo 'building'
    // gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
    // // short SHA, possibly better for chat notifications, etc.
    // shortCommit = gitCommit.take(6)
    // echo(shortCommit)
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
