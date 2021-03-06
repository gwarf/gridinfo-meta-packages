Name:		emi-bdii-site
Version:	1.0.2
Release:	1%{?dist}
Summary:	Metapackage for site BDII 
Group:		Unknown
License:	ASL 2.0
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:     emi-resource-information-service
Requires:     glite-info-provider-ldap
Requires:     bdii-config-site
Requires:     glite-info-site
Requires:     glite-info-static

%description
%{summary}

%prep
%setup -q

%build
rm -rf %{buildroot}
make install prefix=%{buildroot}

%install

%files

%changelog
* Fri Sep 04 2015 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.2-1
- Removing yaim dependency (which is not available in CENTOS7)

* Wed Nov 14 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.1-1
- Depend on emi-resource-information-service

* Mon Nov 12 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.0-1
- Metapackage for emi-bdii-site
