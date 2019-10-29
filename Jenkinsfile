pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build docker image') {
      steps {
        sh 'docker image build -t ${DOCKER_USER}/${DOCKER_IMAGE}:${DOCKER_TAG} .'
      }
    }
    stage('Run docker image') {
      steps {
        sh 'docker run -d -p 80:80 ${DOCKER_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}'
      }
    }
    stage('Push docker image') {
      steps {
        sh 'docker image push ${DOCKER_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}'
      }
    }
  }
  environment {
    DOCKER_USER = 'michalleszczynski'
    DOCKER_TAG = '${BUILD_NUMBER}'
    DOCKER_IMAGE = 'my-web-page'
  }
}