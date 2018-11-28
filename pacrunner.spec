#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pacrunner
Version  : 0.15
Release  : 44
URL      : https://www.kernel.org/pub/linux/network/connman/pacrunner-0.15.tar.xz
Source0  : https://www.kernel.org/pub/linux/network/connman/pacrunner-0.15.tar.xz
Summary  : Proxy Configuration Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: pacrunner-bin
Requires: pacrunner-autostart
Requires: pacrunner-config
Requires: pacrunner-lib
Requires: pacrunner-data
Requires: pacrunner-license
BuildRequires : flex-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libsystemd)
Patch1: 0001-Update-pacrunner-dbus-config.patch
Patch2: 0002-Add-initial-systemd-service-file.patch
Patch3: 0003-Add-a-new-pacdiscovery-V2-service.patch
Patch4: 0004-Use-trimmed-down-glibc-C-locale.patch
Patch5: 0005-Add-port-stripping-for-FindProxyForURL.patch
Patch6: 0006-Don-t-print-out-pointers-for-no-reason.patch

%description
PACrunner - Proxy configuration daemon
**************************************
Compilation and installation
============================

%package autostart
Summary: autostart components for the pacrunner package.
Group: Default

%description autostart
autostart components for the pacrunner package.


%package bin
Summary: bin components for the pacrunner package.
Group: Binaries
Requires: pacrunner-data = %{version}-%{release}
Requires: pacrunner-config = %{version}-%{release}
Requires: pacrunner-license = %{version}-%{release}

%description bin
bin components for the pacrunner package.


%package config
Summary: config components for the pacrunner package.
Group: Default

%description config
config components for the pacrunner package.


%package data
Summary: data components for the pacrunner package.
Group: Data

%description data
data components for the pacrunner package.


%package dev
Summary: dev components for the pacrunner package.
Group: Development
Requires: pacrunner-lib = %{version}-%{release}
Requires: pacrunner-bin = %{version}-%{release}
Requires: pacrunner-data = %{version}-%{release}
Provides: pacrunner-devel = %{version}-%{release}

%description dev
dev components for the pacrunner package.


%package lib
Summary: lib components for the pacrunner package.
Group: Libraries
Requires: pacrunner-data = %{version}-%{release}
Requires: pacrunner-license = %{version}-%{release}

%description lib
lib components for the pacrunner package.


%package license
Summary: license components for the pacrunner package.
Group: Default

%description license
license components for the pacrunner package.


%prep
%setup -q -n pacrunner-0.15
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538062165
%reconfigure --disable-static --enable-duktape \
--disable-mozjs \
--enable-curl \
--enable-debug \
--enable-libproxy
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1538062165
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pacrunner
cp COPYING %{buildroot}/usr/share/doc/pacrunner/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/pacrunner/COPYING.LIB
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m644 src/pacrunner.service %{buildroot}/usr/lib/systemd/system/
install -m644 src/pacdiscovery.service %{buildroot}/usr/lib/systemd/system/
install -m644 src/pacdiscovery.path %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../pacdiscovery.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m644 src/pacdiscovery.conf %{buildroot}/usr/lib/tmpfiles.d/
mkdir -p %{buildroot}/usr/share/dbus-1/system.d
install -m644 src/pacrunner.conf %{buildroot}/usr/share/dbus-1/system.d/
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/pacdiscovery.service %{buildroot}/usr/share/clr-service-restart/pacdiscovery.service
ln -sf /usr/lib/systemd/system/pacrunner.service %{buildroot}/usr/share/clr-service-restart/pacrunner.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/pacdiscovery.path

%files bin
%defattr(-,root,root,-)
/usr/bin/manual-proxy-test
/usr/bin/pacdiscovery
/usr/bin/pacrunner
/usr/bin/proxy

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/pacdiscovery.path
/usr/lib/systemd/system/pacdiscovery.path
/usr/lib/systemd/system/pacdiscovery.service
/usr/lib/systemd/system/pacrunner.service
/usr/lib/tmpfiles.d/pacdiscovery.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/pacdiscovery.service
/usr/share/clr-service-restart/pacrunner.service
/usr/share/dbus-1/system-services/org.pacrunner.service
/usr/share/dbus-1/system.d/pacrunner.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libproxy.so
/usr/lib64/pkgconfig/libproxy-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libproxy.so.1
/usr/lib64/libproxy.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/pacrunner/COPYING
/usr/share/doc/pacrunner/COPYING.LIB
