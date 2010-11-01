%define name python-notify
%define oname notify-python
%define version 0.1.1
%define release %mkrel 6

Summary: Notification system based on libnotify
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.galago-project.org/files/releases/source/notify-python/%{oname}-%{version}.tar.bz2
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

%build
%configure2_5x
touch src/pynotify.override
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%py_platsitedir/gtk-2.0/pynotify/
%_datadir/pygtk/2.0/defs/pynotify.defs
%_libdir/pkgconfig/notify-python.pc


