%global kodi_addon peripheral.joystick
%global kodi_version 17.4
%global kodi_platform_version 17.0

Name:           kodi-peripheral-joystick
Version:        1.3.2
Release:        2%{?dist}
Summary:        Joystick Peripheral addon for Kodi

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/xbmc/%{kodi_addon}/
Source0:        %{url}/archive/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_platform_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Joystick Peripheral Addon for Kodi


%prep
%autosetup -n %{kodi_addon}-%{version} -p0


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Sep 16 2017 Wade Berrier <wberrier@gmail.com> - 1:1.3.2-2
- Minor cleanups from package submission code review

* Thu Aug 17 2017 Wade Berrier <wberrier@gmail.com> - 1:1.3.2-1
- Initial package
