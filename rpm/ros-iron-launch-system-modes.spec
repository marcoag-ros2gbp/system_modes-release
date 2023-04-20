%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-launch-system-modes
Version:        0.9.0
Release:        5%{?dist}%{?release_suffix}
Summary:        ROS launch_system_modes package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-yaml
Requires:       python3
Requires:       ros-iron-ament-index-python
Requires:       ros-iron-launch
Requires:       ros-iron-osrf-pycommon
Requires:       ros-iron-rclpy
Requires:       ros-iron-system-modes-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python3
BuildRequires:  ros-iron-ament-index-python
BuildRequires:  ros-iron-launch
BuildRequires:  ros-iron-osrf-pycommon
BuildRequires:  ros-iron-rclpy
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-system-modes-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
BuildRequires:  ros-iron-ament-flake8
BuildRequires:  ros-iron-ament-pep257
%endif

%description
System modes specific extensions to the launch tool, i.e. launch actions,
events, and event handlers for system modes.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Arne Nordmann <arne.nordmann@de.bosch.com> - 0.9.0-5
- Autogenerated by Bloom

* Wed Mar 22 2023 Arne Nordmann <arne.nordmann@de.bosch.com> - 0.9.0-4
- Autogenerated by Bloom
