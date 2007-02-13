#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-MACD
Summary:	Math::Business::MACD - Perl extension for calculating MACDs
Summary(pl.UTF-8):	Math::Business::MACD - rozszerzenie Perla do obliczania MACD
Name:		perl-Math-Business-MACD
Version:	1.10
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26e11fd1a01d8d3d6dde3f8fec27b1da
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Math-Business-EMA >= 1.06
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::MACD - Perl extension for calculating MACDs.

%description -l pl.UTF-8
Math::Business::MACD - rozszerzenie Perla do obliczania MACD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/Business/MACD.pm
%{_mandir}/man3/*
