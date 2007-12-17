%define name	perl-MP3-ID3v1Tag
%define version 1.11
%define release %mkrel 7

Summary:	MP3-ID3v1Tag module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	MP3-ID3v1Tag-1.11.tar.bz2
URL:		http://www.cpan.org
BuildRequires:	perl-devel
Buildarch:	noarch

%description
MP3-ID3v1Tag module for perl

%prep
%setup -q -n MP3-ID3v1Tag-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/MP3/*
%{_mandir}/*/*

