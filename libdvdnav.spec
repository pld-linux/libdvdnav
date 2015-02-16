#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	DVD menu support library
Summary(pl.UTF-8):	Biblioteka obsługi menu DVD
Name:		libdvdnav
Version:	5.0.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdvdnav/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e9ea4de3bd8f204e61301d407d09f033
Patch0:		%{name}-includes_path.patch
URL:		http://dvdnav.mplayerhq.hu/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libdvdread-devel >= 5.0.2
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
Requires:	libdvdread >= 5.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD menu support library.

%description -l pl.UTF-8
Biblioteka obsługi menu DVD.

%package devel
Summary:	Development files for libdvdnav
Summary(pl.UTF-8):	Pliki potrzebne przy tworzeniu aplikacji korzystających z libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdvdread-devel >= 5.0.2

%description devel
Development files for libdvdnav.

%description devel -l pl.UTF-8
Pliki potrzebne przy tworzeniu aplikacji korzystających z libdvdnav.

%package static
Summary:	Static libdvdnav library
Summary(pl.UTF-8):	Biblioteka statyczna libdvdnav
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdvdnav library.

%description static -l pl.UTF-8
Biblioteka statyczna libdvdnav.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libdvdnav.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvdnav.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/{dvd_structures,library_layout}
%attr(755,root,root) %{_libdir}/libdvdnav.so
%{_libdir}/libdvdnav.la
%{_includedir}/dvdnav
%{_pkgconfigdir}/dvdnav.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvdnav.a
%endif
