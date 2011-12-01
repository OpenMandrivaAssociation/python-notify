%define name python-notify
%define oname notify-python
%define version 0.1.1
%define release %mkrel 9

Summary: Notification system based on libnotify
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.galago-project.org/files/releases/source/notify-python/%{oname}-%{version}.tar.bz2
Patch0: notify-python-0.1.1-libnotify07.patch
Patch1: notify-python-0.1.1-link.patch
License: LGPL
Group: Development/Python
Url: http://www.galago-project.org/news/index.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pygtk2.0-devel
BuildRequires: libnotify-devel
BuildRequires: ffi5-devel

%description
This is the python version of the desktop notification framework.

%prep
%setup -q -n %oname-%version
%patch0 -p1
%patch1 -p0

%build
autoreconf -fi
%configure2_5x
touch src/pynotify.override
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%py_platsitedir/gtk-2.0/pynotify/
%_datadir/pygtk/2.0/defs/pynotify.defs
%_libdir/pkgconfig/notify-python.pc


