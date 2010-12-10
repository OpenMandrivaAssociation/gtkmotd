%define version 0.5
%define release  %mkrel 13
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

