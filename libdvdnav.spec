Summary:	DVD menu support library
Summary(pl):	Biblioteka obs³ugi menu DVD
Name:		libdvdnav
Version:	0.1.0
Release:	2
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
Summary:	Development files for libdvdnav
Summary(pl):	Pliki potrzebne przy tworzeniu aplikacji korzystajacych z libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for libdvdnav.

%description devel -l pl
Pliki potrzebne przy tworzeniu aplikacji korzystajacych z libdvdnav.

%package static
Summary:	Static libdvdnav library
Summary(pl):	Biblioteka statyczna libdvdnav
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libdvdnav library.

%description static -l pl
Biblioteka statyczna libdvdnav.

%prep
%setup -q

%build
rm -f missing
aclocal
autoheader
autoconf
automake -a -c -f
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/dvdnav

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
