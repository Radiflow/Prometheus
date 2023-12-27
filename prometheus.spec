Name:           prometheus
Version:        2.0.0
Release:        1%{?dist}
Summary:        Metric server

License:        Radiflow



BuildRequires:  bash
BuildRequires:  wget
BuildRequires:  docker-ce


Requires:       bash
Requires:       docker-ce

%description
Metric server

%prep
%global __os_install_post %{nil}
rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cd %{_sourcedir}
git clone -b convert-to-docker git@github.com:Radiflow/Prometheus.git
docker pull prom/prometheus:latest
docker tag prom/prometheus:latest prometheus:latest
%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/prometheus/
mkdir -p $RPM_BUILD_ROOT/etc/prometheus/rules/
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/


docker save prometheus:latest | gzip > $RPM_BUILD_ROOT/etc/prometheus/prometheus.tar.gz

cp -r %{_sourcedir}/Prometheus/prometheus/rules/ $RPM_BUILD_ROOT/etc/prometheus/rules
cp %{_sourcedir}/Prometheus/prometheus/prometheus.yml $RPM_BUILD_ROOT/etc/prometheus/prometheus.yml
sudo cp %{_sourcedir}/Prometheus/prometheus/prometheus.service $RPM_BUILD_ROOT/usr/lib/systemd/system/

%post
sudo useradd --no-create-home --shell /bin/false prometheus
sudo groupadd -f prometheus
sudo usermod -a -G docker docker_exporter

chown -R prometheus:prometheus $RPM_BUILD_ROOT/etc/prometheus
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus.service
sudo chmod 664 /usr/lib/systemd/system/prometheus.service

systemctl daemon-reload
systemctl enable prometheus.service
systemctl start prometheus.service


%files
/etc/prometheus/*
/usr/lib/systemd/system/prometheus.service

%clean
rm -rf $RPM_BUILD_ROOT/
docker image rm prom/prometheus:latest

%changelog
* Sun Nov 27 2022 Prometheus
- 
