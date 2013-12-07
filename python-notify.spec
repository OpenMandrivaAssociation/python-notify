%define oname notify-python

Summary:	Notification system based on libnotify
Name:		python-notify
Version:	0.1.1
Release:	14
License:	LGPLv2
Group:		Development/Python
Url:		http://www.galago-project.org/news/index.php
Source0:	http://www.galago-project.org/files/releases/source/notify-python/%{oname}-%{version}.tar.bz2
Patch0:		notify-python-0.1.1-libnotify07.patch
Patch1:		notify-python-0.1.1-link.patch
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(pygtk-2.0)

%description
This is the python version of the desktop notification framework.

%prep
%setup -qn %{oname}-%{version}
%apply_patches
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/g' configure.ac
autoreconf -fi

%build
%configure2_5x
touch src/pynotify.override
%make

%install
%makeinstall_std

%files
%doc NEWS AUTHORS ChangeLog
%{py_platsitedir}/gtk-2.0/pynotify/
%{_datadir}/pygtk/2.0/defs/pynotify.defs
%{_libdir}/pkgconfig/notify-python.pc

