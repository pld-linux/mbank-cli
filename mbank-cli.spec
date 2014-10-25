%include        /usr/lib/rpm/macros.perl
Summary:	A command line interface to mBank
Summary(pl.UTF-8):	Interfejs CLI do mBanku
Name:		mbank-cli
Version:	1.2.2
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Console
Source0:	https://bitbucket.org/jwilk/mbank-cli/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d7510c3084d4fb148d3723e3a0dd51d9
Patch0:		%{name}-ssl_opts.patch
Patch1:		%{name}-ca.patch
URL:		http://code.google.com/p/mbank-cli/
BuildRequires:	perl-base >= 5.10
BuildRequires:	rpm-perlprov
Requires:	ca-certificates
Requires:	perl(LWP::Protocol::https)
Requires:	perl(Net::SSL)
Requires:	perl(Term::ReadLine::Gnu)
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
%patch1 -p1

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
