#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Syntax
%define		pnam	Keyword-Try
Summary:	Syntax::Keyword::Try - a try/catch/finally syntax for Perl
Summary(pl.UTF-8):	Syntax::Keyword::Try - składnia try/catch/finally dla Perla
Name:		perl-Syntax-Keyword-Try
Version:	0.29
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Syntax/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab2b62f3fea1758b9fe7ba031f034864
URL:		https://metacpan.org/dist/Syntax-Keyword-Try
BuildRequires:	perl-Module-Build >= 4.004
BuildRequires:	perl-devel >= 1:5.14.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%{?with_tests:BuildRequires:	perl-Test2-Suite}
BuildRequires:	perl-XS-Parse-Keyword >= 0.06
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a syntax plugin that implements
exception-handling semantics in a form familiar to users of other
languages, being built on a block labeled with the try keyword,
followed by at least one of a catch or finally block.

Syntax similar to this module has now been added to core perl,
starting at version 5.34.0. If you are writing new code, it is
suggested that you instead use the Feature::Compat::Try module
instead, as that will enable the core feature on those supported perl
versions, falling back to Syntax::Keyword::Try on older perls.

%description -l pl.UTF-8
Ten moduł zawiera wtyczkę składniową, implementującą semantykę do
obsługi wyjątków w postaci znanej użytkownikom innych języków,
budowaną w oparciu o blok oznaczny słowem kluczowym "try" z
przynajmniej jednym blokiem "catch" lub "finally".

Składnia podobna do tego modułu została dodana do samego perla,
począwszy od wersji 5.34.0. Przy pisaniu nowego kodu lepiej używać
modułu Feature::Compat::Try, który wykorzysta wsparcie z samego
interpretera w wersjach obsługujących tę składnię, a przy starszych
wykorzysta moduł Syntax::Keyword::Try.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config=optimize="%{rpmcflags}" \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Syntax/Keyword/Try/Try.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Syntax
%dir %{perl_vendorarch}/Syntax/Keyword
%{perl_vendorarch}/Syntax/Keyword/Try.pm
%{perl_vendorarch}/Syntax/Keyword/Try
%dir %{perl_vendorarch}/auto/Syntax
%dir %{perl_vendorarch}/auto/Syntax/Keyword
%dir %{perl_vendorarch}/auto/Syntax/Keyword/Try
%attr(755,root,root) %{perl_vendorarch}/auto/Syntax/Keyword/Try/Try.so
%{_mandir}/man3/Syntax::Keyword::Try*.3pm*
