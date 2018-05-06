#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xenomai
Version  : 3.0.6
Release  : 1
URL      : https://xenomai.org/downloads/xenomai/stable/xenomai-3.0.6.tar.bz2
Source0  : https://xenomai.org/downloads/xenomai/stable/xenomai-3.0.6.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1

BuildRequires : bash
BuildRequires : grep
BuildRequires : fuse-lib
BuildRequires : sudo

%description
Where to start from?
====================
http://xenomai.org/start-here/ is the best place to start learning
about Xenomai 3.

%prep
%setup -q -n xenomai-3.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525528699
scripts/bootstrap
%configure --disable-static --with-core=cobalt --enable-smp --enable-pshared --prefix=/usr/xenomai --includedir=/usr/xenomai/include --bindir=/usr/xenomai/bin --sbindir=/usr/xenomai/bin --with-demodir=/usr/xenomai/demo --libdir=/usr/xenomai/lib64
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1525528699
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/xenomai/*
