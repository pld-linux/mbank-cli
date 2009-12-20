%include        /usr/lib/rpm/macros.perl
Summary:	A command line interface to mBank
Summary(pl.UTF-8):	Interfejs CLI do mBanku
Name:		mbank-cli
Version:	20091208
Release:	2
License:	GPL v2
Group:		Applications/Console
Source0:	http://mbank-cli.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	508cc6366189e29ceaa22e54b24c75c7
Patch0:		%{name}-defconf.patch
URL:		http://code.google.com/p/mbank-cli/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mbank-cli provides a rudimentary command line interface to the mBank
online banking system.

%description -l pl.UTF-8
mbank-cli udostępnia prosty interfejs CLI do systemu bankowości
internetowej mBank.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -D mbank-cli $RPM_BUILD_ROOT%{_bindir}/mbank-cli
install -D doc/mbank-cli.1 $RPM_BUILD_ROOT%{_mandir}/man1/mbank-cli.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/mbank-cli.1*
