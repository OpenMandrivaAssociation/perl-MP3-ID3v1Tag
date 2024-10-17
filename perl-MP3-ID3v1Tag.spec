%define upstream_name	 MP3-ID3v1Tag
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Edit ID3v1 Tags from an Audio MPEG Layer 3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/MP3/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The ID3v1Tag routines are useful for setting and reading ID3 MP3 Audio Tags.
Just create an MP3::ID3v1Tag Object with the path to the file of interest, and
query any of the methods below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/MP3
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 407809
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.11-12mdv2009.0
+ Revision: 257930
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.11-11mdv2009.0
+ Revision: 245958
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-9mdv2008.1
+ Revision: 137191
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-8mdv2008.1
+ Revision: 137004
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill changelog left by repsys


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 19:00:38 (41169)
- rebuild && mkrel

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 18:58:49 (41168)
Import perl-MP3-ID3v1Tag

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.11-6mdk
- fix deps

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.11-5mdk
- rebuild for new perl
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

