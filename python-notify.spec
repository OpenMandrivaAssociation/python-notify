%define oname notify
%define debug_package %nil

Summary:	Notification system based on libnotify
Name:		python-notify
Version:	0.3.1
Release:	7
License:	LGPLv2
Group:		Development/Python
Url:		https://pypi.org/project/notify/
Source0:	https://files.pythonhosted.org/packages/source/n/notify/notify-%{version}.tar.gz
Patch0:		notify-0.3.1-no-setuptools-2to3.patch
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools

%description
This is the python version of the desktop notification framework.

%prep
%autosetup -p1 -n %{oname}-%{version}
2to3 -w src/notify/*.py

%build
%py_build

%install
%py_install

%files
%{_bindir}/notify
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py*.egg-info
