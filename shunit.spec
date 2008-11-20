Summary:	shunit
Name:		shunit
Version:	1.3
Release:	0.1
License:	GPL v2
Group:		Development/Building
Source0:	http://dl.sourceforge.net/shunit/ShUnit-%{version}.tgz
# Source0-md5:	3c91026c2e6e8598f2e14e38f0455881
URL:		http://shunit.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n ShUnit-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
