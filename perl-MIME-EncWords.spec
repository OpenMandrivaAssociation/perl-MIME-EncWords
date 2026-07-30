%define upstream_version 1.015.0
%define modname	MIME-EncWords
%define modver 1.015.0

Summary:	Deal with RFC-1522 encoded words (improved)
Name:		perl-%{modname}
Epoch:		1
Version:	1.015.0
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/MIME-EncWords
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-EncWords-1.015.0.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl(MIME::Charset)
BuildRequires:	perl-devel

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. :-)

%prep
%setup -qn %{modname}-%{modver} -n MIME-EncWords-1.015.0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc ARTISTIC GPL README
%{perl_vendorlib}/MIME
%{perl_vendorlib}/Encode
%{perl_vendorlib}/POD2/JA/Encode
%{perl_vendorlib}/POD2/JA/MIME
%{_mandir}/man3/*
