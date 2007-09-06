#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DVD menu support library
Summary(pl.UTF-8):	Biblioteka obsługi menu DVD
Name:		libdvdnav
Version:	0.1.10
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/dvd/%{name}-%{version}.tar.gz
# Source0-md5:	c8ddee96ba1182d73447eaf0bb6fde81
Patch0:		%{name}-opt.patch
URL:		http://dvd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel >= 0.9.3
BuildRequires:	libtool
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
Requires:	libdvdread-devel

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
	--enable-static \
	%{!?with_static_libs:--disable-static}
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
%{_aclocaldir}/*.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%endif
