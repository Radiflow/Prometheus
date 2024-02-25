pipeline {
  agent {
      label 'redhat' 
  }
  environment
  {
    versionMajor = 1
    versionMinor = 0
    versionPatch = 0
    newVersion = "${versionMajor}.${versionMinor}.${versionPatch}"
  } 
  stages
  {
    stage('Build-Container')
    {
      steps
      {
        script {
          docker.image("10.0.2.6:8083/docker_builder:isolate").inside("--privileged"){
            withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
              './scripts/build-container.sh ${isid} ${icen} ${newVersion} $USERNAME $PASSWORD'
          }
        }
      }
    }
  }
}
