%define upstream_name    Hash-Flatten
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Flatten/unflatten complex data hashes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Log::Trace)
BuildRequires: perl(Test::Assertions)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Converts back and forth between a nested hash structure and a flat hash of
delimited key-value pairs. Useful for protocols that only support key-value
pairs (such as CGI and DBMs).

Functional interface
    * $flat_hash = flatten($nested_hash, \%options)

      Reduces a nested data-structure to key-value form. The top-level
      container must be hashref. For example:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


