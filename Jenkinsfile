pipeline {
  agent any
  stages {
    stage('Remove old docker images') {
      steps {
        sh 'docker container stop $(docker container ls |grep my-web-page| cut -d' ' -f1)'
        sh 'docker container rm $(docker container ls |grep my-web-page| cut -d' ' -f1'
        sh 'docker image rm $(docker image ls | grep my-web-page | cut -d' ' -f1)'
      }
    }
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
