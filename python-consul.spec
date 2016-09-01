Name:             python-consul
Version:          0.6.1
Release:          1.eayun%{?dist}
Summary:          Python API and CLI for Consul

Group:            Application
License:          GPL
URL:              https://github.com/cablehead/%{name}
Source0:          python-consul-%{version}.tar.gz


BuildRequires:  /bin/bash
BuildRequires:  python
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:   python

%description
Consul client tool

%prep
%setup -q



%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc
#%{_bindir}/consul
%{python_sitelib}/*.egg-info
/usr/lib/python2.7/site-packages/

%changelog
* Thu Sep 1 2016 Chen Yuanbin <cybing4@gmail.com> 0.6.1-1
  Add Make file, Add python-consul.spec file
  Remove aio.py module file
