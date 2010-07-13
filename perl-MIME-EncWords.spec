%define upstream_name     MIME-EncWords
%define upstream_version 1.012

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1
Epoch:          1

Summary:        Deal with RFC-1522 encoded words (improved)
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl(MIME::Charset)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. :-)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


