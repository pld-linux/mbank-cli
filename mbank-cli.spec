%include		/usr/lib/rpm/macros.perl
Summary:	A command line interface to mBank
Summary(pl.UTF-8):	Interfejs CLI do mBanku
Name:		mbank-cli
Version:	1.6
Release:	1
Epoch:		1
License:	MIT
Group:		Applications/Console
Source0:	https://bitbucket.org/jwilk/mbank-cli/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7ce7f351f7fadd0b4d45f3d44d4ebc6b
Patch0:		%{name}-ca.patch
URL:		http://jwilk.net/software/mbank-cli
BuildRequires:	perl-base >= 5.10
BuildRequires:	rpm-perlprov
Requires:	ca-certificates
Requires:	perl(Term::ReadLine::Gnu)
Requires:	perl-HTML-Form
Requires:	perl-HTML-Parser
Requires:	perl-HTML-Tree
Requires:	perl-HTTP-Cookies
Requires:	perl-HTTP-Message
Requires:	perl-IO-Socket-SSL
Requires:	perl-IPC-Run
Requires:	perl-LWP-Protocol-https
Requires:	perl-Net-HTTP
Requires:	perl-Net-SSLeay
Requires:	perl-TimeDate
Requires:	perl-libwww
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
%attr(755,root,root) %{_bindir}/mbank-cli
%{_mandir}/man1/mbank-cli.1*
