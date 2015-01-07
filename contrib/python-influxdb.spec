%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           python-influxdb
Version:        0.1.13
Release:        1%{?dist}
Summary:        Python client for interacting with InfluxDB

Group:          Development/Languages
License:        MIT
URL:            https://github.com/influxdb/influxdb-python
Source0:        https://pypi.python.org/packages/source/i/influxdb/influxdb-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-requests

%description
Python client for interacting with InfluxDB.


%prep
%setup -q -n influxdb-%{version}


%build
%{__python} setup.py build


%install
[ "%{buildroot}" != / ] && %{__rm} -rf "%{buildroot}"
%{__python} setup.py install -O1 --skip-build --root "%{buildroot}"


%clean
[ "%{buildroot}" != / ] && %{__rm} -rf "%{buildroot}"


%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*


%changelog
* Fri Dec 26 2014 Jiri Tyr <jiri.tyr@gmail.com> 0.1.3-1
- Initial package
