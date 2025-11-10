Summary:	A command line interface to mBank
Summary(pl.UTF-8):	Interfejs CLI do mBanku
Name:		mbank-cli
Version:	2.6.4
Release:	1
Epoch:		1
License:	MIT
Group:		Applications/Console
Source0:	https://github.com/jwilk/mbank-cli/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	52b97d638e3551afec57b174f3cf9e57
Patch0:		%{name}-ca.patch
URL:		http://jwilk.net/software/mbank-cli
BuildRequires:	perl-base >= 1:5.14
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
Requires:	ca-certificates
Requires:	perl-base >= 1:5.14
Requires:	perl-HTML-Form
Requires:	perl-HTML-Tree >= 5
Requires:	perl-IO-Socket-SSL >= 1:1.81
Requires:	perl-IPC-Run
Requires:	perl-LWP-Protocol-https
Requires:	perl-Net-HTTP
Requires:	perl-Net-SSLeay >= 1.43
Requires:	perl-Term-ReadLine-Gnu
Requires:	perl-libwww >= 6
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
%patch -P0 -p1

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' mbank-cli

%build
%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -D mbank-cli $RPM_BUILD_ROOT%{_bindir}/mbank-cli
install -D doc/mbank-cli.1 $RPM_BUILD_ROOT%{_mandir}/man1/mbank-cli.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE doc/README
%attr(755,root,root) %{_bindir}/mbank-cli
%{_mandir}/man1/mbank-cli.1*
