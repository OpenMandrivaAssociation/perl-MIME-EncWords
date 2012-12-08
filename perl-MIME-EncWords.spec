%define upstream_name     MIME-EncWords
%define upstream_version 1.012.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	Deal with RFC-1522 encoded words (improved)
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	 perl(MIME::Charset)
BuildRequires:	 perl-devel
BuildArch:	noarch

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. :-)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.12.3-3mdv2012.0
+ Revision: 765482
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.12.3-2
+ Revision: 763976
- rebuilt for perl-5.14.x

* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.12.3-1
+ Revision: 685814
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.12.0-3
+ Revision: 667232
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1:1.12.0-2mdv2011.0
+ Revision: 564737
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.12.0-1mdv2011.0
+ Revision: 552409
- update to 1.012

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.11.1-1mdv2010.1
+ Revision: 399734
- bumping epoch to take new version into account
- update to 1.011.1 for real this time
- using %%perl_convert_version
- fixed license field

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.011.1-1mdv2010.0
+ Revision: 387011
- update to new version 1.011.1

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.011-1mdv2010.0
+ Revision: 377834
- update to new version 1.011

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.010.101-2mdv2009.0
+ Revision: 265416
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.010.101-1mdv2009.0
+ Revision: 196827
- update to new version 1.010.101

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.010.1-1mdv2009.0
+ Revision: 194860
- update to new version 1.010.1

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.010-1mdv2009.0
+ Revision: 193861
- update to new version 1.010

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.04.0-2mdv2008.1
+ Revision: 180434
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04.0-1mdv2007.0
+ Revision: 86557
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03.2-1mdv2007.1
+ Revision: 84308
- fix doc files
- Import perl-MIME-EncWords

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03.2-1mdv2007.1
- first mdv release

