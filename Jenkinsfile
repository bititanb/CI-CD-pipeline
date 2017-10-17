#!/usr/bin/env groovy

node('master') {
  stage('Checkout'){
      checkout([
          $class: 'GitSCM',
          branches: [[name: '*/master']],
          doGenerateSubmoduleConfigurations: false,
          extensions: [[$class: 'RelativeTargetDirectory',
          relativeTargetDir: '/tmp/taskmngr-django']],
          submoduleCfg: [],
          userRemoteConfigs: [[url: 'https://github.com/bititanb/CI-CD-pipeline']]
      ])
    // ansiblePlaybook(
    //     playbook: "/etc/ansible/taskmngr.yaml",
    //     tags: 'taskmngr-kubernetes',
    //     extraVars: [
    //       app_checkout: "true",
    //     ]
    // )
  }
  stage('Build'){
    ansiblePlaybook(
        playbook: "/etc/ansible/taskmngr.yaml",
        tags: 'taskmngr-kubernetes',
        extraVars: [
          app_build: "true",
        ]
    )
  }
  stage('Deploy testing'){
    ansiblePlaybook(
        playbook: "/etc/ansible/taskmngr.yaml",
        tags: 'taskmngr-kubernetes',
        extraVars: [
          app_deploy_testing: "true",
        ]
    )
  }
  stage('Tests'){
    ansiblePlaybook(
        playbook: "/etc/ansible/taskmngr.yaml",
        tags: 'taskmngr-kubernetes',
        extraVars: [
          app_test: "true",
        ]
    )
  }
  stage('Deploy prod'){
    ansiblePlaybook(
        playbook: "/etc/ansible/taskmngr.yaml",
        tags: 'taskmngr-kubernetes',
        extraVars: [
          app_deploy_prod: "true",
        ]
    )
  }
}
