Summary:	DVD menu support library
Summary(pl):	Biblioteka obs³ugi menu DVD
Name:		libdvdnav
Version:	0.1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/dvd/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD menu support library.

%description -l pl
Biblioteka obs³ugi menu DVD.

%package devel
Summary:	Headers
Summary(pl):	Nag³ówki
Group:		Development/Libraries
Requires:	%{name}-%{version}

%description devel
Header files for libdvdnav.

%description devel -l pl
Pliki nag³ówkowe dla libdvdnav.

%prep
%setup -q
#%patch0 -p1

%build
rm missing
aclocal
autoheader
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/*.la
%{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so
%{_includedir}/dvdnav
