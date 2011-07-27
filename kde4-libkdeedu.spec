%define         _state          stable
%define		orgname		libkdeedu
%define         qtver           4.7.3

Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		libkdeedu
Version:	4.7.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	10e59e1b68ffa940637a16369fef88da
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	kde4-libkdeedu
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

%description devel
Header files for libkdeedu development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdeedu.

%prep
%setup -q

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
