%define         _state          stable
%define		orgname		libkdeedu
%define         qtver           4.8.0

Summary:	Libraries used by KDE education applications
Summary(pl.UTF-8):	Biblioteki używane przez aplikacje edukacyjne KDE
Name:		kde4-libkdeedu
Version:	4.11.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	54af01f8326a9da07c79e748a69c88e1
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	libkdeedu < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Edu library.

%description -l pl.UTF-8
Biblioteka KDE Edu.

%package devel
Summary:	Header files for libkdeedu development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkdeedu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kdeedu-devel < 4.8.0

%description devel
Header files for libkdeedu development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdeedu.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkeduvocdocument.so.?
%attr(755,root,root) %{_libdir}/libkeduvocdocument.so.*.*.*
%{_datadir}/apps/kvtml
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_iconsdir}/hicolor/scalable/actions/*.svgz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkeduvocdocument.so
%{_includedir}/libkdeedu
%{_libdir}/cmake/libkdeedu
%{_libdir}/libqtmmlwidget.a
