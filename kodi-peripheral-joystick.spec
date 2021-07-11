%global kodi_addon peripheral.joystick
%global kodi_codename Matrix
%global kodi_version 19.0

Name:           kodi-peripheral-joystick
Version:        1.7.2
Release:        1%{?dist}
Summary:        Joystick Peripheral addon for Kodi

License:        GPLv2+
URL:            https://github.com/xbmc/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(tinyxml)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
Joystick Peripheral Addon for Kodi.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md docs/CONTRIBUTING.md
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.1-2
- Rebuild for Kodi 19 RC1

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Wed Aug 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

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
