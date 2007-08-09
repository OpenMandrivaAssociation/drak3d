%define drakxtools_required_version  10.4.90-1mdv2007.0
%define drakxtools_conflicted_version  10.4.89

%define libname %mklibname %{name}

Summary:  3D desktop effects tools
Name:     drak3d
Version:  1.5
Release:  %mkrel 1
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Hardware
Url:      http://wiki.mandriva.com/en/Docs/Desktop/Accelerated_Desktop
BuildRequires: perl-MDK-Common-devel gettext
Requires: drakxtools-backend => %drakxtools_required_version
BuildRoot: %_tmppath/%name-%version-buildroot
# for program:
Conflicts: drakxtools <= %drakxtools_conflicted_version
# for man pages:
Conflicts: drakxtools-curses <= %drakxtools_conflicted_version
BuildArch: noarch

%description
Drak3d enables to configure 3D desktop effects.

%prep
%setup -q

%build
%make

%install
rm -fr %{buildroot}
%makeinstall_std

#install lang
%find_lang %name

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d

cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/29drak3d <<EOF
NAME=drak3d
ICON=drak3d.png
EXEC=/usr/sbin/drak3d
DESC=3D Desktop effects configuration
SCRIPT:
exec /usr/sbin/drak3d
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_sbindir}/*
/usr/lib/libDrakX/icons/*
%{_sysconfdir}/X11/wmsession.d/29drak3d
/usr/lib/libDrakX/Xconfig/glx.pm


