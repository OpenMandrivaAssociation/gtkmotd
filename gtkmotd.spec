Summary: 	Message of the day display
Name: 		gtkmotd
Version: 	0.5
Release: 	15
License: 	GPL
URL: 		http://rhlx01.rz.fht-esslingen.de/gtkmotd/
Group: 		Toys
Source: 	%{name}-%{version}.tar.bz2
BuildRequires:	libgtk+-devel

%description
gtkmotd displays the message of the day as of /etc/motd to the user and
exits. It is useful to have in X11 startup scripts.

%prep

%setup

%build
%make

%install
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/gtkmotd
Name=Gtkmotd
Comment=Gtk version of motd
Comment[ru]=Gtk-версия motd
Icon=other_configuration
Categories=Settings;
EOF

%files
%doc AUTHORS CHANGELOG COPYING README TODO
%{_bindir}/gtkmotd
%{_datadir}/applications/mandriva-*.desktop



