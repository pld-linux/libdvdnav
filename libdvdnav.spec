Summary:	DVD menu support library
Summary(pl):	Biblioteka obs³ugi menu DVD
Name:		libdvdnav
Version:	0.1.9
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/dvd/%{name}-%{version}.tar.gz
# Source0-md5: 5b0d168d87f66f8c8d7b2b51e16ff9d8
Patch0:		%{name}-opt.patch
URL:		http://dvd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel >= 0.9.3
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD menu support library.

%description -l pl
Biblioteka obs³ugi menu DVD.

%package devel
Summary:	Development files for libdvdnav
Summary(pl):	Pliki potrzebne przy tworzeniu aplikacji korzystaj±cych z libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libdvdread-devel

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
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/lib*.la
%{_includedir}/dvdnav

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
