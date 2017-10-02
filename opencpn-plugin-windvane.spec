%global commit 35e4b328d098f574c67a3f7a844dbc8b0f4c58c6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner jongough
%global project windvane_pi
%global plugin windvane

Name: opencpn-plugin-%{plugin}
Summary: Windvane autopilot plugin for OpenCPN
Version: 0.0.5
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: cmake
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: gtk3-devel
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}

%description
Windvane autopilot for OpenCPN.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%files

%{_libdir}/opencpn/lib%{plugin}_pi.so
