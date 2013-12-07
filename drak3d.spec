Summary:	3D desktop effects tools
Name:		drak3d
Version:	1.29
Release:	12
License:	GPLv2
Group:		System/Configuration/Hardware
Url:		http://wiki.mandriva.com/en/Docs/Desktop/Accelerated_Desktop
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools-backend
# we need the common pam usermode config files
Requires:	usermode-consoleonly

%description
Drak3d enables to configure 3D desktop effects.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

#install lang
%find_lang %{name}

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d

cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/29drak3d <<EOF
NAME=drak3d
ICON=drak3d.png
EXEC=/usr/sbin/drak3d
DESC=3D Desktop effects configuration
SCRIPT:
exec /usr/sbin/drak3d
EOF

# consolehelper config
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/drak3d
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat > %{buildroot}%{_sysconfdir}/security/console.apps/drak3d <<EOF
USER=<user>
PROGRAM=/usr/sbin/drak3d
FALLBACK=false
SESSION=true
EOF

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
ln -sf %{_sysconfdir}/pam.d/mandriva-simple-auth %{buildroot}%{_sysconfdir}/pam.d/drak3d

%files -f %{name}.lang
%doc COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/pam.d/drak3d
%config(noreplace) %{_sysconfdir}/security/console.apps/drak3d
%{_bindir}/drak3d
%{_sbindir}/*
/usr/lib/libDrakX/icons/*
%{_sysconfdir}/X11/wmsession.d/29drak3d
/usr/lib/libDrakX/Xconfig/glx.pm

