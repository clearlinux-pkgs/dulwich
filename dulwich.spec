#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dulwich
Version  : 0.19.6
Release  : 3
URL      : https://files.pythonhosted.org/packages/fc/1b/c499026353d48cbf45e325017da2246110802c5095c99c903cb70ba68102/dulwich-0.19.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/1b/c499026353d48cbf45e325017da2246110802c5095c99c903cb70ba68102/dulwich-0.19.6.tar.gz
Summary  : [![Build Status](https://travis-ci.org/dulwich/dulwich.png?branch=master)](https://travis-ci.org/dulwich/dulwich)
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: dulwich-bin
Requires: dulwich-python3
Requires: dulwich-license
Requires: dulwich-python
Requires: certifi
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : gevent
BuildRequires : urllib3

%description
Openstack Swift as backend for Dulwich
======================================
Fabien Boucher <fabien.boucher@enovance.com>

%package bin
Summary: bin components for the dulwich package.
Group: Binaries
Requires: dulwich-license

%description bin
bin components for the dulwich package.


%package license
Summary: license components for the dulwich package.
Group: Default

%description license
license components for the dulwich package.


%package python
Summary: python components for the dulwich package.
Group: Default
Requires: dulwich-python3

%description python
python components for the dulwich package.


%package python3
Summary: python3 components for the dulwich package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dulwich package.


%prep
%setup -q -n dulwich-0.19.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534122606
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dulwich
cp COPYING %{buildroot}/usr/share/doc/dulwich/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dul-receive-pack
/usr/bin/dul-upload-pack
/usr/bin/dulwich

%files license
%defattr(-,root,root,-)
/usr/share/doc/dulwich/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
