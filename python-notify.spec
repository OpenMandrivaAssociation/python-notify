%define oname notify-python

Summary:	Notification system based on libnotify
Name:		python-notify
Version:	0.1.1
Release:	11
Source0:	http://www.galago-project.org/files/releases/source/notify-python/%{oname}-%{version}.tar.bz2
Patch0:		notify-python-0.1.1-libnotify07.patch
Patch1:		notify-python-0.1.1-link.patch
License:	LGPL
Group:		Development/Python
Url:		http://www.galago-project.org/news/index.php
BuildRequires:	pygtk2.0-devel
BuildRequires:	libnotify-devel
BuildRequires:	ffi5-devel

%description
This is the python version of the desktop notification framework.

%prep
%setup -q -n %oname-%version
%patch0 -p1
%patch1 -p0

%build
sed -i -e 's/AM_CONFIG_HEADER/AM_CONFIG_HEADERS/g' configure.ac
autoreconf -fi
%configure2_5x
touch src/pynotify.override
%make

%install
%makeinstall_std

%files
%doc NEWS AUTHORS ChangeLog
%py_platsitedir/gtk-2.0/pynotify/
%_datadir/pygtk/2.0/defs/pynotify.defs
%_libdir/pkgconfig/notify-python.pc




%changelog
* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.1.1-7mdv2011.0
+ Revision: 650839
- add fedora patch to make it build with latest libnotify

* Mon Nov 01 2010 Jani Välimaa <wally@mandriva.org> 0.1.1-6mdv2011.0
+ Revision: 591681
- rebuild for python 2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-5mdv2010.1
+ Revision: 523839
- rebuilt for 2010.1

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.1-4mdv2009.1
+ Revision: 319468
- rebuild with python 2.6

* Mon Sep 01 2008 Tiago Salem <salem@mandriva.com.br> 0.1.1-3mdv2009.0
+ Revision: 278648
- fix BuildRequires to libffi
- force regeneration of pynotify.c. fixes attach_to_status_icon bug
- bump release

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-2mdv2009.0
+ Revision: 225135
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.1-1mdv2008.1
+ Revision: 136454
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2007.0
+ Revision: 107828
- Import python-notify

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2007.1
- initial package

