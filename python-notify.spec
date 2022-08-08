%define oname notify
%define debug_package %nil

Summary:	Notification system based on libnotify
Name:		python-notify
Version:	0.3.1
Release:	3
License:	LGPLv2
Group:		Development/Python
Url:		http://www.galago-project.org/news/index.php
Source0:	https://files.pythonhosted.org/packages/5e/ee/392ea0366a8d1389e6321697b26b3d98f0d828161a0a2ead4d1fa21dfc44/notify-0.3.1.tar.gz
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
%rename	python-notify

%description
This is the python version of the desktop notification framework.

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/notify
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py*.egg-info

