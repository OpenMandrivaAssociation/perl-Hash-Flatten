%define upstream_name    Hash-Flatten
%define upstream_version 1.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Flatten/unflatten complex data hashes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Log::Trace)
BuildRequires:	perl(Test::Assertions)
BuildArch:	noarch

%description
Converts back and forth between a nested hash structure and a flat hash of
delimited key-value pairs. Useful for protocols that only support key-value
pairs (such as CGI and DBMs).

Functional interface
    * $flat_hash = flatten($nested_hash, \% options)

      Reduces a nested data-structure to key-value form. The top-level
      container must be hashref. For example:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.190.0-2mdv2011.0
+ Revision: 656929
- rebuild for updated spec-helper

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 596529
- update to new version 1.19

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 471400
- import perl-Hash-Flatten


* Sun Nov 29 2009 cpan2dist 1.16-1mdv
- initial mdv release, generated with cpan2dist
