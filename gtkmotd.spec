%define version 0.5
%define release  14
%define name gtkmotd

Summary: 	Message of the day display
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
URL: 		http://rhlx01.rz.fht-esslingen.de/gtkmotd/
Group: 		Toys
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+-devel

%description
gtkmotd displays the message of the day as of /etc/motd to the user and
exits. It is useful to have in X11 startup scripts.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
%make

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application <<EOF
Exec=/usr/bin/gtkmotd
Name=Gtkmotd
Comment=Gtk version of motd
Icon=other_configuration
Categories=Settings;
EOF
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS CHANGELOG COPYING README TODO
%{_bindir}/gtkmotd
%{_datadir}/applications/mandriva-*.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-13mdv2011.0
+ Revision: 619290
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-12mdv2010.0
+ Revision: 429339
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5-11mdv2009.0
+ Revision: 246700
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.5-9mdv2008.1
+ Revision: 131740
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gtkmotd


* Fri Jan 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.5-9mdk
- fix build on x86-64

* Sat Nov 06 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.5-8mdk
- add BuildRequires: libgtk+-devel

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5-7mdk
- rebuild

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-6mdk
- rebuild

* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5-5mdk
- Fix menu entry

* Wed Jul 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5-4mdk
- rebuild

* Thu Jan 11 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- rebuild
- add url

* Mon Sep 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- BM
- macros
- menu


* Tue Feb 29 2000 Adrian Reber <adrian@linux-mandrake.com>
- Mandrake adaptations.
 
* Thu Mar 04 1999 Nils Philippsen <nils@fht-esslingen.de>
- Rebuilt against gtk+-1.2.0
 
* Tue Dec 22 1998 Nils Philippsen <nils@fht-esslingen.de>
- Rebuilt against gtk+-1.1.7
 
* Mon Dec 07 1998 Nils Philippsen <nils@fht-esslingen.de>
- Initial build of version 0.5   
