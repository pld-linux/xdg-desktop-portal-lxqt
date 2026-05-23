#
# Conditional build:
#
%define         qtver           6.6.0

Summary:	A backend implementation for xdg-desktop-portal that is using Qt/KF6/libfm-qt
Summary(pl.UTF-8):	Implementacja backendu dla xdg-desktop-portal wykorzystująca Qt/KF6/libfm-qt
Name:		xdg-desktop-portal-lxqt
Version:	1.4.0
Release:	1
License:	LGPL-2.0-or-later
URL:		https://lxqt-project.org
Source0:	https://github.com/lxqt/xdg-desktop-portal-lxqt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e624e0c130c2210a7e3a08ab6d9b6e04
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	libexif-devel
BuildRequires:	libfm-qt-devel >= 2.4.0
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	dbus
Requires:	xdg-desktop-portal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A backend implementation for xdg-desktop-portal that is using
Qt/KF6/libfm-qt

%description -l pl.UTF-8
Implementacja backendu dla xdg-desktop-portal wykorzystująca
Qt/KF6/libfm-qt

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_desktopdir}/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/xdg-desktop-portal/lxqt-portals.conf
%{_libexecdir}/xdg-desktop-portal-lxqt
%{systemduserunitdir}/%{name}.service

%clean
rm -rf $RPM_BUILD_ROOT
