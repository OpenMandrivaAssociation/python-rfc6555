Name:		python-rfc6555
Version:	0.1.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/r/rfc6555/rfc6555-%{version}.tar.gz
Summary:	Python implementation of the Happy Eyeballs Algorithm described in RFC 6555.
URL:		https://pypi.org/project/rfc6555/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python implementation of the Happy Eyeballs Algorithm described in RFC 6555.

%prep
%autosetup -p1 -n rfc6555-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/rfc6555.py
%{py_sitedir}/rfc6555-*.*-info
