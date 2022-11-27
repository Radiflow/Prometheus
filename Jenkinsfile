pipeline {
  agent {
    kubernetes {
      defaultContainer 'rpm-builder'
      yamlFile 'pod-configuration.yml'
    }
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
            sh 'mv prometheus-2.40.2.linux-amd64 prometheus-0.0.1'
            sh 'mv /home/jenkins/agent/workspace/prometheus/prometheus.yml prometheus-0.0.1' 
            sh 'tar --create --file prometheus-0.0.1.tar.gz prometheus-0.0.1'
            sh 'mv prometheus-0.0.1.tar.gz rpmbuild/SOURCES'
            sh 'mv prometheus.spec rpmbuild/SPECS'
            sh 'rpmlint ~/rpmbuild/SPECS/prometheus.spec'
            sh 'rpmbuild -ba ~/rpmbuild/SPEC/prometheus.spec'
            sh 'tree rpmbuild'
          }             
        }
      }
    }
  }
}
