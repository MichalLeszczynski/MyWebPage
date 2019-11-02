pipeline {
  agent any
  stages {
    stage('Build docker image') {
      steps {
        sh 'docker image build -t ${DOCKER_USER}/${DOCKER_IMAGE}:1.0.${BUILD_NUMBER} .'
      }
    }
    stage('Run docker image') {
      steps {
        sh 'docker run -d -p 80:80 ${DOCKER_USER}/${DOCKER_IMAGE}:1.0.${BUILD_NUMBER}'
      }
    }
    stage('Push docker image') {
      steps {
        withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
          sh 'docker image push ${DOCKER_USER}/${DOCKER_IMAGE}:1.0.${BUILD_NUMBER}'
        }
      }
    }
  }
  environment {
    DOCKER_USER = 'michalleszczynski'
    DOCKER_TAG = '${BUILD_NUMBER}'
    DOCKER_IMAGE = 'my-web-page'
  }
}
