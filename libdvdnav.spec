Summary:	DVD menu support library
Summary(pl):	Biblioteka obs³ugi menu DVD
Name:		libdvdnav
Version:	0.1.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/dvd/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://dvd.sourceforge.net/

%description
DVD menu support library.

%description -l pl
Biblioteka obs³ugi menu DVD.

%package devel
Summary:	Development files for libdvdnav
Summary(pl):	Pliki potrzebne przy tworzeniu aplikacji korzystaj±cych z libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for libdvdnav.

%description devel -l pl
Pliki potrzebne przy tworzeniu aplikacji korzystaj±cych z libdvdnav.

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
libtoolize --copy --force
aclocal
autoheader
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
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
