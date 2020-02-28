#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x579C160D4C9E23E8 (jelmer@fsfe.org)
#
Name     : dulwich
Version  : 0.19.15
Release  : 20
URL      : https://files.pythonhosted.org/packages/61/9e/975cd95e7b15f71ff29307a02fc61d232d07cc3b66519ca43aceff0cde10/dulwich-0.19.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/9e/975cd95e7b15f71ff29307a02fc61d232d07cc3b66519ca43aceff0cde10/dulwich-0.19.15.tar.gz
Source1  : https://files.pythonhosted.org/packages/61/9e/975cd95e7b15f71ff29307a02fc61d232d07cc3b66519ca43aceff0cde10/dulwich-0.19.15.tar.gz.asc
Summary  : Python Git Library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: dulwich-bin = %{version}-%{release}
Requires: dulwich-license = %{version}-%{release}
Requires: dulwich-python = %{version}-%{release}
Requires: dulwich-python3 = %{version}-%{release}
Requires: certifi
Requires: fastimport
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : fastimport
BuildRequires : gevent
BuildRequires : urllib3

%description
.. image:: https://travis-ci.org/dulwich/dulwich.png?branch=master
  :alt: Build Status
  :target: https://travis-ci.org/dulwich/dulwich

.. image:: https://ci.appveyor.com/api/projects/status/mob7g4vnrfvvoweb?svg=true
  :alt: Windows Build Status
  :target: https://ci.appveyor.com/project/jelmer/dulwich/branch/master

This is the Dulwich project.

It aims to provide an interface to git repos (both local and remote) that
doesn't call out to git directly but instead uses pure Python.

**Main website**: <https://www.dulwich.io/>

**License**: Apache License, version 2 or GNU General Public License, version 2 or later.

The project is named after the part of London that Mr. and Mrs. Git live in
in the particular Monty Python sketch.

Installation
------------

By default, Dulwich' setup.py will attempt to build and install the optional C
extensions. The reason for this is that they significantly improve the performance
since some low-level operations that are executed often are much slower in CPython.

If you don't want to install the C bindings, specify the --pure argument to setup.py::

    $ python setup.py --pure install

or if you are installing from pip::

    $ pip install dulwich --global-option="--pure"

Note that you can also specify --global-option in a
`requirements.txt <https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers>`_
file, e.g. like this::

    dulwich --global-option=--pure

Getting started
---------------

Dulwich comes with both a lower-level API and higher-level plumbing ("porcelain").

For example, to use the lower level API to access the commit message of the
last commit::

    >>> from dulwich.repo import Repo
    >>> r = Repo('.')
    >>> r.head()
    '57fbe010446356833a6ad1600059d80b1e731e15'
    >>> c = r[r.head()]
    >>> c
    <Commit 015fc1267258458901a94d228e39f0a378370466>
    >>> c.message
    'Add note about encoding.\n'

And to print it using porcelain::

    >>> from dulwich import porcelain
    >>> porcelain.log('.', max_entries=1)
    --------------------------------------------------
    commit: 57fbe010446356833a6ad1600059d80b1e731e15
    Author: Jelmer Vernooĳ <jelmer@jelmer.uk>
    Date:   Sat Apr 29 2017 23:57:34 +0000

    Add note about encoding.

Further documentation
---------------------

The dulwich documentation can be found in docs/ and built by running ``make
doc``. It can also be found `on the web <https://www.dulwich.io/docs/>`_.

Help
----

There is a *#dulwich* IRC channel on the `Freenode <https://www.freenode.net/>`_, and
`dulwich-announce <https://groups.google.com/forum/#!forum/dulwich-announce>`_
and `dulwich-discuss <https://groups.google.com/forum/#!forum/dulwich-discuss>`_
mailing lists.

Contributing
------------

For a full list of contributors, see the git logs or `AUTHORS <AUTHORS>`_.

If you'd like to contribute to Dulwich, see the `CONTRIBUTING <CONTRIBUTING.rst>`_
file and `list of open issues <https://github.com/dulwich/dulwich/issues>`_.

Supported versions of Python
----------------------------

At the moment, Dulwich supports (and is tested on) CPython 2.7, 3.4, 3.5, 3.6,
3.7 and Pypy.

%package bin
Summary: bin components for the dulwich package.
Group: Binaries
Requires: dulwich-license = %{version}-%{release}

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
Requires: dulwich-python3 = %{version}-%{release}

%description python
python components for the dulwich package.


%package python3
Summary: python3 components for the dulwich package.
Group: Default
Requires: python3-core
Provides: pypi(dulwich)

%description python3
python3 components for the dulwich package.


%prep
%setup -q -n dulwich-0.19.15
cd %{_builddir}/dulwich-0.19.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582921119
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dulwich
cp %{_builddir}/dulwich-0.19.15/COPYING %{buildroot}/usr/share/package-licenses/dulwich/9e9b8604dc428d3f50acf86a2e36d56e008672d6
python3 -tt setup.py build  install --root=%{buildroot}
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dulwich/9e9b8604dc428d3f50acf86a2e36d56e008672d6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
