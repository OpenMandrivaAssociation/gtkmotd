%define version 0.5
%define release 9mdk
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

(cd $RPM_BUILD_ROOT
mkdir -p .%{_menudir}
cat > .%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/gtkmotd"\
title="Gtkmotd"\
longtitle="Gtk version of motd"\
needs="x11"\
icon="other_configuration.png"\
section="System/Configuration/Other"
EOF
)
 
%post
%{update_menus}
 
%postun
%{clean_menus} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS CHANGELOG COPYING README TODO
%{_bindir}/gtkmotd
%{_menudir}/*

