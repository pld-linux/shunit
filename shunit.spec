Summary:	xUnit based unit testing for Unix shell scripts
Name:		shunit
Version:	2.1.5
Release:	0.2
License:	LGPL 2.1
Group:		Development/Building
Source0:	http://shunit2.googlecode.com/files/%{name}2-%{version}.tgz
# Source0-md5:	f434f0095f7ca9a698ade330feae356a
URL:		http://code.google.com/p/shunit2/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.
If you have ever had the desire to write a unit test for a shell
script, shUnit2 can do the job.

%prep
%setup -q -n %{name}2-%{version}
rm -f doc/LGPL-2.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install src/shell/shunit2 $RPM_BUILD_ROOT%{_bindir}/%{name}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/shunit
%{_examplesdir}/%{name}-%{version}
