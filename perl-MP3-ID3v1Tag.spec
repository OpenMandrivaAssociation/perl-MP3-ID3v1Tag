%define module	MP3-ID3v1Tag
%define name	perl-%{module}
%define version 1.11
%define release %mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Edit ID3v1 Tags from an Audio MPEG Layer 3
License:	GPL or Artistic
Group:		Development/Perl
Source0:	MP3-ID3v1Tag-1.11.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/MP3/%{module}-%{version}.tar.bz2
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The ID3v1Tag routines are useful for setting and reading ID3 MP3 Audio Tags.
Just create an MP3::ID3v1Tag Object with the path to the file of interest, and
query any of the methods below.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/MP3
%{_mandir}/*/*

