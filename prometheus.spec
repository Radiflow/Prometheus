Name:           prometheus
Version:        0.0.1
Release:        1%{?dist}
Summary:        Metric server

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash 

%description
Metric server

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
useradd --no-create-home --shell /bin/false prometheus
mkdir /etc/prometheus
mkdir /var/lib/prometheus
chown prometheus:prometheus /etc/prometheus
chown prometheus:prometheus /var/lib/prometheus
ls
ls /root/rpmbuild/BUILDROOT/
cp prometheus /%{_bindir}
cp prometheus $RPM_BUILD_ROOT/usr/local/bin
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/local/bin/prometheus
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/bin/prometheus

cp promtool $RPM_BUILD_ROOT/%{_bindir}
cp promtool $RPM_BUILD_ROOT/usr/local/bin
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/local/bin/promtool
chown prometheus:prometheus $RPM_BUILD_ROOT/usr/bin/promtool

cp -r consoles $RPM_BUILD_ROOT/etc/prometheus
cp -r console_libraries $RPM_BUILD_ROOT/etc/prometheus
chown -R prometheus:prometheus $RPM_BUILD_ROOT/etc/prometheus/consoles
chown -R prometheus:prometheus $RPM_BUILD_ROOT/etc/prometheus/console_libraries

cp prometheus.service $RPM_BUILD_ROOT/etc/systemd/system


%post
systemctl daemon-reload
systemctl start prometheus

%files
/etc/prometheus/*
/var/lib/prometheus/*
/usr/local/bin/prometheus
/usr/bin/prometheus
/usr/local/bin/promtool
/usr/bin/promtool
/etc/systemd/system/prometheus.service



%changelog
* Sun Nov 27 2022 Prometheus
- 
