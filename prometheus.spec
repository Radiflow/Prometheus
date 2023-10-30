Name:           prometheus
Version:        1.0.1
Release:        1%{?dist}
Summary:        Metric server

License:        GPL
Source0:        %{name}-%{version}.tar.gz


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
git clone git@github.com:Radiflow/Prometheus.git
docker pull prom/prometheus:latest
docker pull prom/alertmanager:latest

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/prometheus/
mkdir -p $RPM_BUILD_ROOT/etc/alertmanager/
mkdir -p $RPM_BUILD_ROOT/etc/alertmanager/rules/
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/


docker save prom/prometheus:latest | gzip > $RPM_BUILD_ROOT/etc/prometheus/prometheus.tar.gz
docker save prom/alertmanager:latest | gzip > $RPM_BUILD_ROOT/etc/alertmanager/alertmanager.tar.gz

cp -r %{_sourcedir}/Prometheus/prometheus/rules/ $RPM_BUILD_ROOT/etc/prometheus/rules
cp %{_sourcedir}/Prometheus/alertmanager/alertmanager.yml $RPM_BUILD_ROOT/etc/alertmanager/alertmanager.yml
cp %{_sourcedir}/Prometheus/prometheus/prometheus.yml $RPM_BUILD_ROOT/etc/prometheus/prometheus.yml
sudo cp %{_sourcedir}/Prometheus/prometheus.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
sudo cp %{_sourcedir}/Prometheus/alertmanager.service $RPM_BUILD_ROOT/usr/lib/systemd/system/

%post
sudo useradd --no-create-home --shell /bin/false prometheus
sudo groupadd -f prometheus
sudo usermod -a -G docker docker_exporter

chown -R prometheus:prometheus $RPM_BUILD_ROOT/etc/prometheus
chown -R prometheus:prometheus $RPM_BUILD_ROOT/etc/alertmanager
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus.service
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/lib/systemd/system/alertmanager.service
sudo chmod 664 /usr/lib/systemd/system/prometheus.service
sudo chmod 664 /usr/lib/systemd/system/alertmanager.service

systemctl daemon-reload
systemctl enable alertmanager.service
systemctl enable prometheus.service
systemctl start alertmanager.service
systemctl start prometheus.service


%files
/etc/prometheus/*
/etc/alertmanager/*
/usr/lib/systemd/system/prometheus.service
/usr/lib/systemd/system/alertmanager.service

%clean
rm -rf $RPM_BUILD_ROOT/
docker image rm prom/prometheus:latest
docker image rm prom/alertmanager:latest

%changelog
* Sun Nov 27 2022 Prometheus
- 
