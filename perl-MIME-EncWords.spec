%define modname	MIME-EncWords
%define modver 1.014.2

Summary:	Deal with RFC-1522 encoded words (improved)
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/MIME/MIME-EncWords-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(MIME::Charset)
BuildRequires:	perl-devel

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. :-)

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ARTISTIC GPL README
%{perl_vendorlib}/MIME
%{perl_vendorlib}/Encode
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/5.16.3/POD2/JA/Encode/MIME/EncWords.pod
%{_libdir}/perl5/vendor_perl/5.16.3/POD2/JA/MIME/EncWords.pod


