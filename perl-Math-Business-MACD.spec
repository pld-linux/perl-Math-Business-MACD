#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-MACD
Summary:	Math::Business::MACD - Perl extension for calculating MACDs
Summary(pl):	Math::Business::MACD - rozszerzenie Perla do obliczania MACD
Name:		perl-Math-Business-MACD
Version:	1.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-Business-EMA >= 1.05
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::MACD - Perl extension for calculating MACDs.

%description -l pl
Math::Business::MACD - rozszerzenie Perla do obliczania MACD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Math/Business/MACD.pm
%{_mandir}/man3/*
