%define module  MIME-EncWords
%define name    perl-%{module}
%define version 1.010.1
%define up_version  0.040
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Deal with RFC-1522 encoded words (improved)
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/MIME/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRequires:  perl(MIME::Charset)
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. :-)

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc ARTISTIC GPL README
%{perl_vendorlib}/MIME
%{_mandir}/*/*


