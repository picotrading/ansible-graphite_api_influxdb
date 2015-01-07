%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           python-graphite-influxdb
Version:        0.4
Release:        3%{?dist}
Summary:        An InfluxDB backend for Graphite Web or Graphite API

Group:          Development/Languages
License:        BSD
URL:            https://github.com/vimeo/graphite-influxdb
Source0:        https://pypi.python.org/packages/source/g/graphite-influxdb/graphite-influxdb-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-anyjson
Requires:       python-flask-cache
Requires:       python-influxdb

%description
An InfluxDB (0.8-rc5 or higher) backend for Graphite Web (source or
0.10.x) or Graphite API.


%prep
%setup -q -n graphite-influxdb-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*


%changelog
* Wed Jan 7 2015 Jiri Tyr <jiri.tyr at gmail.com> 0.4-3
- Removing graphite-api from the dependency list.

* Tue Jan 6 2015 Jiri Tyr <jiri.tyr at gmail.com> 0.4-2
- Adding graphite-api, python-graphite-api, python-influxdb and
  python-flask-cache into the dependency list.

* Fri Dec 26 2014 Jiri Tyr <jiri.tyr@gmail.com> 0.4-1
- Initial package
