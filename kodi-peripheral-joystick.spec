%global kodi_addon peripheral.joystick
%global kodi_version 18.0
%global kodi_platform_version 18.0

Name:           kodi-peripheral-joystick
Version:        1.4.6
Release:        3%{?dist}
Summary:        Joystick Peripheral addon for Kodi

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/xbmc/%{kodi_addon}/
Source0:        %{url}/archive/v%{version}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_platform_version}
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
Joystick Peripheral Addon for Kodi


%prep
%autosetup -n %{kodi_addon}-%{version}


%build
%cmake -DSTEAMLINK=1
%make_build


%install
%make_install


%files
%doc Readme.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.6-2
- Enable arm build

* Thu Aug 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Wade Berrier <wberrier@gmail.com> - 1.3.2-3
- add additional BuildRequires: pcre-devel systemd-devel

* Sat Sep 16 2017 Wade Berrier <wberrier@gmail.com> - 1:1.3.2-2
- Minor cleanups from package submission code review

* Thu Aug 17 2017 Wade Berrier <wberrier@gmail.com> - 1:1.3.2-1
- Initial package
