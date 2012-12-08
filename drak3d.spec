%define drakxtools_required_version  10.4.90-1mdv2007.0
%define drakxtools_conflicted_version  10.4.89

Summary:  3D desktop effects tools
Name:     drak3d
Version:  1.29
Release:  %mkrel 4
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Hardware
Url:      http://wiki.mandriva.com/en/Docs/Desktop/Accelerated_Desktop
BuildRequires: perl-MDK-Common-devel gettext
Requires: drakxtools-backend => %drakxtools_required_version
# we need the common pam usermode config files
Requires: usermode-consoleonly >= 1.92-4mdv2008.0
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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/pam.d/drak3d
%config(noreplace) %{_sysconfdir}/security/console.apps/drak3d
%{_bindir}/drak3d
%{_sbindir}/*
/usr/lib/libDrakX/icons/*
%{_sysconfdir}/X11/wmsession.d/29drak3d
/usr/lib/libDrakX/Xconfig/glx.pm



%changelog
* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.29-2mdv2011.0
+ Revision: 604814
- rebuild

* Wed May 26 2010 Anne Nicolas <ennael@mandriva.org> 1.29-1mdv2010.1
+ Revision: 546166
- update translations

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 1.28-1mdv2010.1
+ Revision: 499976
- install glxinfo instead of mesa-demos

* Thu Oct 15 2009 Olivier Blin <oblin@mandriva.com> 1.27-1mdv2010.0
+ Revision: 457581
- 1.27
- allow to detect installed 3D compositing_types (for finish-install)

* Wed Oct 14 2009 Olivier Blin <oblin@mandriva.com> 1.26-1mdv2010.0
+ Revision: 457245
- 1.26
- show compiz choice before metisse
- drop Xgl support

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.25.2-2mdv2010.0
+ Revision: 413376
- rebuild

* Tue Apr 21 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.25.2-1mdv2009.1
+ Revision: 368564
- 1.25.2:
- don't blacklist vbox video driver anymore since vbox 2.2 supports 3D accel

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 1.25.1-1mdv2009.1
+ Revision: 367397
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 1.25-1mdv2009.1
+ Revision: 362308
- translation updates

* Fri Nov 14 2008 Olivier Blin <oblin@mandriva.com> 1.24-1mdv2009.1
+ Revision: 303161
- 1.24
- allow to show only installed WMs in interactive mode
  (for finish-install)

* Thu Nov 13 2008 Olivier Blin <oblin@mandriva.com> 1.23-1mdv2009.1
+ Revision: 302715
- 1.23
- add --force option to force 3D desktop enabling even if not supported

* Wed Nov 12 2008 Olivier Blin <oblin@mandriva.com> 1.22-1mdv2009.1
+ Revision: 302549
- 1.22
- check if system supports command line options before applying them
- blacklist geode driver

* Wed Nov 12 2008 Olivier Blin <oblin@mandriva.com> 1.21-1mdv2009.1
+ Revision: 302520
- 1.21
- do not die in automatic mode if there is no control terminal

* Fri Nov 07 2008 Olivier Blin <oblin@mandriva.com> 1.20-1mdv2009.1
+ Revision: 300391
- 1.20
- set gstreamer videosink to ximagesink when using 3D desktop
  (based on patch from Caio Begotti, #25572)
- add --auto/--method=<method>/--wm=<wm> command line options

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 1.19-1mdv2009.0
+ Revision: 290094
- translation updates

* Wed Sep 17 2008 Olivier Blin <oblin@mandriva.com> 1.18-1mdv2009.0
+ Revision: 285514
- 1.18
- new icons

* Wed Sep 03 2008 Olivier Blin <oblin@mandriva.com> 1.17-1mdv2009.0
+ Revision: 279780
- 1.17
- KDE4 support

* Tue Aug 05 2008 Olivier Blin <oblin@mandriva.com> 1.16-1mdv2009.0
+ Revision: 264007
- 1.16
- blacklist openchrome: it doesn't actually support compiz yet
  (from Adam Williamson, #38379)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.15-2mdv2009.0
+ Revision: 220682
- rebuild

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 1.15-1mdv2008.1
+ Revision: 192160
- translation updates

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 1.14-1mdv2008.1
+ Revision: 190114
- translation updates

* Thu Feb 14 2008 Anssi Hannula <anssi@mandriva.org> 1.13-1mdv2008.1
+ Revision: 168660
- 1.13
  o drop fglrx from blacklist, glxinfo hang has been fixed

* Mon Feb 11 2008 Olivier Blin <oblin@mandriva.com> 1.12-2mdv2008.1
+ Revision: 165471
- do not run update-menus without menu file (thanks rpmlint)
- 1.12
- blacklist fglrx driver (it makes glxinfo hang, #37269)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.11-2mdv2008.1
+ Revision: 149213
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 05 2007 Olivier Blin <oblin@mandriva.com> 1.11-1mdv2008.0
+ Revision: 95608
- 1.11
- blacklist vesa driver

* Thu Oct 04 2007 Olivier Blin <oblin@mandriva.com> 1.10-1mdv2008.0
+ Revision: 95453
- 1.10
- blacklist vboxvideo driver

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 1.9-1mdv2008.0
+ Revision: 95035
- updated translation
- updated translation

* Sat Sep 29 2007 Olivier Blin <oblin@mandriva.com> 1.8-1mdv2008.0
+ Revision: 93906
- 1.8
- blacklist cards using mga driver when detecting 3D capabilities (#33985)

* Thu Sep 27 2007 Thierry Vignaud <tv@mandriva.org> 1.7-1mdv2008.0
+ Revision: 93285
- updated translation
- updated translations

* Wed Sep 12 2007 Andreas Hasenack <andreas@mandriva.com> 1.5-3mdv2008.0
+ Revision: 84826
- use new common pam config files for usermode/consolehelper

* Wed Aug 29 2007 Andreas Hasenack <andreas@mandriva.com> 1.5-2mdv2008.0
+ Revision: 74706
- allow authenticated console user to run drak3d as root

* Thu Aug 09 2007 Olivier Blin <oblin@mandriva.com> 1.5-1mdv2008.0
+ Revision: 60806
- 1.5: use Compiz Fusion as label for 3D cube desktop

* Wed Aug 08 2007 Olivier Blin <oblin@mandriva.com> 1.4-1mdv2008.0
+ Revision: 60451
- 1.4: use Compiz Fusion instead of compiz and beryl

* Fri Jun 08 2007 Thierry Vignaud <tv@mandriva.org> 1.3-1mdv2008.0
+ Revision: 37055
- first release after SVN recover


* Sat Mar 31 2007 Olivier Blin <oblin@mandriva.com> 1.2-1mdv2007.1
+ Revision: 150099
- 1.2: install aquamarine for KDE and heliodor for Gnome when beryl is selected

* Thu Mar 29 2007 Olivier Blin <oblin@mandriva.com> 1.1-1mdv2007.1
+ Revision: 149282
- 1.1: fix server selection

* Fri Mar 23 2007 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2007.1
+ Revision: 148673
- 1.0
- update URL

* Sat Mar 10 2007 Olivier Blin <oblin@mandriva.com> 0.9-2mdv2007.1
+ Revision: 140950
- disable warnings (by not forgetting to run make like Titi did :-p)

* Wed Mar 07 2007 Olivier Blin <oblin@mandriva.com> 0.9-1mdv2007.1
+ Revision: 134817
- 0.9 (compiz-decorator-kde support and UI fixes)

* Tue Mar 06 2007 Olivier Blin <oblin@mandriva.com> 0.8-1mdv2007.1
+ Revision: 133848
- 0.8

* Fri Mar 02 2007 Olivier Blin <oblin@mandriva.com> 0.7-2mdv2007.1
+ Revision: 131085
- fix group (#29046)

* Wed Feb 28 2007 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2007.1
+ Revision: 129307
- 0.7
- cosmetics

* Fri Jan 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6-2mdv2007.1
+ Revision: 110908
- relax requires on drakxtools; we don't need gtk+ and the like

* Fri Jan 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6-1mdv2007.1
+ Revision: 110898
- do use translations

* Fri Jan 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2007.1
+ Revision: 110740
- drak3d is splited in its own package
- add buildrequires
- Import drak3d

