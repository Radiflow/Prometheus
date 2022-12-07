pipeline {
  agent {
    kubernetes {
      defaultContainer 'rpm-builder'
      yamlFile 'pod-configuration.yml'
    }
  }
  environment
  {
    NEXUS=credentials('nexus')    
  } 
  stages
  {
    stage('Build-RPM')
    {
      steps
      {
        container('rpm-builder')
        {
          dir(path: '/home/jenkins/agent/workspace') {
            sh 'wget https://github.com/prometheus/prometheus/releases/download/v2.40.2/prometheus-2.40.2.linux-amd64.tar.gz'
            sh 'tar -xvf prometheus-2.40.2.linux-amd64.tar.gz'
            sh 'rpmdev-setuptree'
            sh 'mkdir prometheus-0.0.1'
            sh 'cp -r prometheus-2.40.2.linux-amd64/* prometheus-0.0.1'
            sh 'ls prometheus-0.0.1'
            sh 'mv Prometheus/prometheus.yml prometheus-0.0.1' 
            sh 'mv Prometheus/prometheus.service prometheus-0.0.1'
            sh 'tar --create --file prometheus-0.0.1.tar.gz prometheus-0.0.1'
            sh 'cp prometheus-0.0.1.tar.gz ~/rpmbuild/SOURCES'
            sh 'ls ~/rpmbuild/SOURCES'
            sh 'mv Prometheus/prometheus.spec ~/rpmbuild/SPECS'
            sh 'rpmlint ~/rpmbuild/SPECS/prometheus.spec'
            sh 'rpmbuild -ba ~/rpmbuild/SPECS/prometheus.spec'
            sh 'ls ~/rpmbuild/RPMS/x86_64/'
            sh 'curl -v -u $NEXUS_USR:$NEXUS_PSW --upload-file ~/rpmbuild/RPMS/x86_64/prometheus-0.0.1-1.el8.x86_64.rpm http://10.0.2.6:8081/repository/centos8/Prometheus/$BUILD_NUMBER/prometheus-1.0.0-1.el8.x86_64.rpm'
          }             
        }
      }
    }
  }
}
