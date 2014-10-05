%define rubyver 1.9

%define build_goocanvas 1

Summary:	Set of Ruby language bindings for the GNOME 2.0
Name:		ruby-gnome2
Version:	2.2.0
Release:	2
License:	LGPLv2+
Group:		Development/Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0: 	http://surfnet.dl.sourceforge.net/sourceforge/ruby-gnome2/%{name}-all-%{version}.tar.gz

BuildRequires:	ruby-devel
BuildRequires:	rubygem(pkg-config)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem(cairo)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.90)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
#BuildConflicts:	gtksourceview1.0
BuildConflicts:	xulrunner-devel

Requires:	ruby >= %{rubyver}
#Requires:	ruby-libart2 = %version
Requires:	rubygem(gtk2)
#Requires:	ruby-gnomecanvas2 = %version

%description
This is a set of Ruby language bindings for the GNOME 2.0 development
environment. This is the next generation of Ruby-GNOME.

%package devel
Summary:	Headers for developing with Ruby/Gnome2, Ruby/Gtk2, 
License:	LGPLv2+
Group:		Development/Ruby
Requires:	%{name} = %{version}-%{release}
Provides:	ruby-gtk2-devel
Requires:	pkgconfig(gdk-pixbuf-2.0)
Requires:	pkgconfig(gtk+-2.0)
Requires:	pkgconfig(pango)

%description devel
Ruby bindings for Gnome2.
This package contains header files needed for developing Ruby extensions
depending on Ruby/Gnome2, Ruby/Glib2, Ruby/Pango, ...

%package -n ruby-gtk3
Summary:        Ruby binding of gtk-3.0.x
Group:          Development/Ruby

%description -n ruby-gtk3
Ruby/Gtk3 is a Ruby binding of gtk-3.0.x.

%package -n ruby-gdk3
Summary:        Ruby binding of gdk-3.0.x
Group:          Development/Ruby

%description -n ruby-gdk3
Ruby/Gdk3 is a Ruby binding of gdk-3.0.x.

%package -n ruby-cairo-gobject
Summary:        Ruby binding of cairo-gobject
Group:          Development/Ruby
Requires:       rubygem(gtk2)

%description -n ruby-cairo-gobject
Ruby/CairoGobject is a Ruby binding of cairo-gobject.

%package -n ruby-gtksourceview2
Summary:	Ruby binding of gtksourceview-2.0.x
Group:		Development/Ruby
Requires:	rubygem(gtk2)

%description -n ruby-gtksourceview2
Ruby/GtkSourceView is a Ruby binding of gtksourceview-2.0.x.

%package -n ruby-gtksourceview3
Summary:        Ruby binding of gtksourceview-3.0.x
Group:          Development/Ruby

%description -n ruby-gtksourceview3
Ruby/GtkSourceView is a Ruby binding of gtksourceview-3.0.x.

%package -n ruby-gst
Summary:	Ruby binding of GStreamer
Group:		Development/Ruby
Requires:	rubygem(glib2)
  	 
%description -n ruby-gst
Ruby/GStreamer is a Ruby binding of GStreamer.

%package -n ruby-rsvg2
Summary:        Ruby binding of Rsvg2
Group:          Development/Ruby
Requires:       rubygem(glib2)

%description -n ruby-rsvg2
Ruby/Rsvg2 is a Ruby binding of Rsvg2.

%package -n ruby-vte3
Summary:        Ruby binding of Vte3
Group:          Development/Ruby

%description -n ruby-vte3
Ruby/Vte3 is a Ruby binding of vte3.

%if %{build_goocanvas}
%package -n ruby-goocanvas
Summary:	Ruby binding of goocanvas
Group:		Development/Ruby
BuildRequires:	goocanvas-devel

%description -n ruby-goocanvas
Ruby/BonoboUI2 is a Ruby binding of goocanvas.
%endif


%prep 
%setup -q -n ruby-gnome2-all-%{version}
#find -name depend -exec sed -i s/sitearchdir/vendorarchdir/ {} \;

%build
#ruby extconf.rb --vendor
ruby extconf.rb 
%make

find */* -name \*.rb -exec sed -i -e 's|/usr/local/bin/ruby|/usr/bin/ruby|' {} \;

%install
make install DESTDIR=%{buildroot} libdir=%buildroot%{_libdir} archdir=%{buildroot}%{ruby_sitearchdir}

mkdir -p %buildroot%{_bindir}

for f in `find */test */tests */sample */samples -type f`
do
        if head -n1 "$f" | grep '^#!' >/dev/null;
        then
                sed -i 's|/usr/local/bin|/usr/bin|' "$f"
                chmod 0755 "$f"
        else
                chmod 0644 "$f"
        fi
done

## Remove files packaged from gems
rm -rf %{buildroot}%{ruby_sitelibdir}/gnome2

# ruby-gobject-introspection
rm -f %{buildroot}%{ruby_sitearchdir}/gobject_introspection.so
rm -rf %{buildroot}%{ruby_sitelibdir}/gobject-introspection
rm -f %{buildroot}%{ruby_sitelibdir}/gobject-introspection.rb

# ruby-glib2
rm -f %{buildroot}%{ruby_sitearchdir}/glib2.so
rm -f %{buildroot}%{ruby_sitelibdir}/glib2.rb
rm -rf %{buildroot}%{ruby_sitelibdir}/glib2
rm -f %{buildroot}%{ruby_sitelibdir}/glib-mkenums.rb
rm -f %{buildroot}glib/{COPYING.LIB,ChangeLog,README}

# ruby-gtk2
rm -f %{buildroot}%{ruby_sitearchdir}/gtk2.so
rm -f %{buildroot}%{ruby_sitelibdir}/gtk2.rb
rm -rf %{buildroot}%{ruby_sitelibdir}/gtk2
rm -rf %{buildroot}gtk/{COPYING.LIB,ChangeLog,README,sample}

# ruby-gdkpixbuf2
rm -f %{buildroot}%{ruby_sitearchdir}/gdk_pixbuf2.so
rm -f %{buildroot}%{ruby_sitelibdir}/gdk_pixbuf2.rb
rm -rf %{buildroot}gdkpixbuf/{COPYING.LIB,ChangeLog,README,sample}

# ruby-gio2
rm -f %{buildroot}%{ruby_sitearchdir}/gio2.so
rm -f %{buildroot}%{ruby_sitelibdir}/gio2.rb
rm -rf %{buildroot}%{ruby_sitelibdir}/gio2

# ruby-pango
rm -f %{buildroot}%{ruby_sitearchdir}/pango.so
rm -f %{buildroot}%{ruby_sitelibdir}/pango.rb
rm -rf %{buildroot}pango/{COPYING.LIB,ChangeLog,README,sample}

# ruby-atk
rm -f %{buildroot}%{ruby_sitearchdir}/atk.so
rm -f %{buildroot}%{ruby_sitelibdir}/atk.rb
rm -f %{buildroot}atk/{COPYING.LIB,ChangeLog,README}

# ruby-vte
rm -f %{buildroot}%{ruby_sitearchdir}/vte.so
rm -f %{buildroot}%{ruby_sitelibdir}/vte.rb
rm -rf %{buildroot}vte/{ChangeLog,README,sample,COPYING.LIB}
rm -rf %{buildroot}%{ruby_sitelibdir}/vte

# ruby-poppler
rm -f %{buildroot}%{ruby_sitearchdir}/poppler.so
rm -f %{buildroot}%{ruby_sitelibdir}/poppler.rb
rm -rf %{buildroot}poppler/{ChangeLog,README,sample,COPYING.LIB}



%files
%doc AUTHORS COPYING.LIB NEWS README
%{ruby_sitelibdir}/gnome2-*.rb
%{ruby_sitelibdir}/mkmf-gnome2.rb

%files -n ruby-cairo-gobject
%{ruby_sitearchdir}/cairo_gobject.so
%{ruby_sitelibdir}/cairo-gobject.rb
%doc AUTHORS cairo-gobject/{README.md,COPYING.LIB}

%files -n ruby-gdk3
%{ruby_sitearchdir}/gdk3.so
%{ruby_sitelibdir}/gdk3.rb
%{ruby_sitelibdir}/gdk3
%doc AUTHORS gdk3/{README.md,COPYING.LIB}

%files -n ruby-gtk3
%{ruby_sitearchdir}/gtk3.so
%{ruby_sitelibdir}/gtk3.rb
%{ruby_sitelibdir}/gtk3
%doc AUTHORS gtk3/{README.md,COPYING.LIB,sample}

%files -n ruby-gtksourceview2
%{ruby_sitearchdir}/gtksourceview2.so
%{ruby_sitelibdir}/gtksourceview2.rb
%doc AUTHORS gtksourceview2/{README,sample,COPYING.LIB}

%files -n ruby-rsvg2
%{ruby_sitearchdir}/rsvg2.so
%{ruby_sitelibdir}/rsvg2.rb
%doc AUTHORS rsvg2/{README,sample,COPYING.LIB}

%files -n ruby-gtksourceview3
%{ruby_sitearchdir}/gtksourceview3.so
%{ruby_sitelibdir}/gtksourceview3.rb
%{ruby_sitelibdir}/gtksourceview3
%doc AUTHORS gtksourceview3/{sample,COPYING.LIB,README.md}

%files -n ruby-vte3
%{ruby_sitearchdir}/vte3.so
%{ruby_sitelibdir}/vte3.rb
%{ruby_sitelibdir}/vte3
%doc AUTHORS vte3/{sample,COPYING.LIB,README.md}

%files devel
# Seems to be no longer installed and needed
#{ruby_sitelibdir}/mkmf-gnome2.rb
#{ruby_sitelibdir}/pkg-config.rb
%{ruby_sitearchdir}/*.h
#%{_libdir}/pkgconfig

%files -n ruby-gst 	 
%{ruby_sitearchdir}/gstreamer.so 	 
%{ruby_sitelibdir}/gst.rb
%{ruby_sitelibdir}/gst
%doc AUTHORS gstreamer/{COPYING.LIB,README.md}

%if %build_goocanvas
%files -n ruby-goocanvas
%doc goocanvas/README
%{ruby_sitelibdir}/goocanvas.rb
%{ruby_sitearchdir}/goocanvas.so
%{ruby_sitelibdir}/goo
%endif


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.19.2-4mdv2011.0
+ Revision: 669458
- mass rebuild

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.19.2-3mdv2011.0
+ Revision: 626200
- fix build with poppler 0.16.0
- rebuild for new poppler

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19.2-2mdv2011.0
+ Revision: 488801
- rebuilt against libjpeg v8

* Wed Sep 23 2009 Pascal Terjan <pterjan@mandriva.org> 0.19.2-1mdv2010.0
+ Revision: 447715
-  Ship pkgconfig files
- Update to 0.19.2

  + Guillaume <gc@mandriva.com>
    - new version 0.19.1

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-5mdv2010.0
+ Revision: 417193
- rebuilt against libjpeg v7

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 0.19.0-4mdv2010.0
+ Revision: 384754
- rebuild for new vte

* Thu Jun 04 2009 Götz Waschk <waschk@mandriva.org> 0.19.0-3mdv2010.0
+ Revision: 382884
- add missing dep
- update license
- add support for building with goocanvas
- update build deps

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.19.0-2mdv2010.0
+ Revision: 382207
- rebuild for new libvte

* Sat May 30 2009 Götz Waschk <waschk@mandriva.org> 0.19.0-1mdv2010.0
+ Revision: 381188
- new version
- drop patches
- fix format string

  + Pascal Terjan <pterjan@mandriva.org>
    - Fix build
    - Add support for panel applet without libgnomeui from upstream svn

* Thu Nov 27 2008 Pascal Terjan <pterjan@mandriva.org> 0.18.1-1mdv2009.1
+ Revision: 307297
- Update to 0.18.1
- Build gtksourceview2 instead of gtksourceview1

* Sat Sep 13 2008 Pascal Terjan <pterjan@mandriva.org> 0.17.0-1mdv2009.0
+ Revision: 284394
- BuildRequires pkgconfig(gstreamer-plugins-base-0.10)
- Add ruby-bonobo2 and ruby-bonoboui2
- Disable gtkmozembed for now
- Update to 0.17
- Add back GStreamer binding

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16.0-8mdv2009.0
+ Revision: 217947
- add dependencies to the -devel package

* Wed Jun 11 2008 Pascal Terjan <pterjan@mandriva.org> 0.16.0-7mdv2009.0
+ Revision: 217822
- Move back to site dir, vendor is not supported enough yet :(

* Tue Jun 10 2008 Pascal Terjan <pterjan@mandriva.org> 0.16.0-6mdv2009.0
+ Revision: 217767
- Move .h in vendor dir even if site is hardcoded
- Adapt upstream poppler 0.7 patch
- Move to vendor

  + Thierry Vignaud <tv@mandriva.org>
    - improved description

* Mon Apr 14 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.16.0-5mdv2009.0
+ Revision: 193275
- BuildRequires: libcairo-devel, as pointed by Guillaume Cottenceau

* Sun Feb 17 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.16.0-4mdv2008.1
+ Revision: 169546
- P8: fix for build with glib2.0-2.15.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - P7: security fix for CVE-2007-6183

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot
    - fix summary-ended-with-dot

* Mon Sep 24 2007 Pascal Terjan <pterjan@mandriva.org> 0.16.0-3mdv2008.0
+ Revision: 92696
- Fix BuildRequires
- Fix build with recent glib/poppler/... (P2,P3,P4,P5,P6)
- Remove BuildRequires on libgstreamer0.8-devel, gst binding is no longer part of ruby-GNOME2


* Wed Feb 28 2007 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2007-02-28 19:40:32 (127335)
- fix gdk-pixbuf build dependency

* Tue Jan 02 2007 Pascal Terjan <pterjan@mandriva.org> 0.16.0-1mdv2007.1
+ 2007-01-02 17:51:46 (103014)
- Include ruby-gtkmozembed
- Use global ruby macros
- Drop patch0
- 0.16.0
- ADD 2 patchs from CVS
- Use Development/Ruby
- Add Ruby/Poppler
- Drop Ruby/GStreamer and Ruby/Libgda
- Import ruby-gnome2

* Mon Jul 17 2006 Guillaume Cottenceau 0.15.0-2mdv2007.0
- don't abort when ruby program using gtk2.rb has passed arguments

* Mon Jul 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.15.0-1mdv2007.0
- 0.15.0
- %%mkrel
- deactivate ruby-libgda2, it doesn't build (problem to fix)

* Wed Dec 28 2005 Pascal Terjan <pterjan@mandriva.org> 0.14.1-2mdk
- BuildRequires libgstreamer0.8-devel as other versions won't work

* Mon Nov 14 2005 Pascal Terjan <pterjan@mandriva.org> 0.14.1-1mdk
- 0.14.1
- Disable gtkmozembed for now, it's still a separate package so 
  that we do not need to rebuild ruby-gnome2 on new firefox versions

* Wed Oct 26 2005 Pascal Terjan <pterjan@mandriva.org> 0.14.0-1mdk
- 0.14.0
- Drop patch0 (merged upstream)
- Fix permissions on samples

* Sun Oct 09 2005 Pascal Terjan <pterjan@mandriva.org> 0.13.0-3mdk
- The patch was useless if not build against new gnomecanvas :/

* Tue Sep 20 2005 Pascal Terjan <pterjan@mandriva.org> 0.13.0-2mdk
- Patch ruby-gnomecanvas to not break if people install gnome 2.12

* Mon Aug 01 2005 Guillaume Cottenceau <gc@mandrakesoft.com> 0.13.0-1mdk
- 0.13.0

* Sun Mar 06 2005 Pascal Terjan <pterjan@mandrake.org> 0.12.0-1mdk
- 0.12.0
- Remove dots at the end of summaries
- Remove release in requires
- /usr/local/bin/ruby -> /usr/bin/ruby in samples

* Sun Nov 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.11.0-1mdk
- 0.11.0
- Become rpmbuildupdate aware
- New packages : gnomeprint2/gnomeprintui2/rsvg2

* Mon Aug 16 2004 Pascal Terjan <pterjan@mandrake.org> 0.10.1-1mdk
- 0.10.1
- Drop patch0 (merged upstream)

* Mon Aug 09 2004 Pascal Terjan <pterjan@mandrake.org> 0.10.0-1mdk
- 0.10.0 
- Merged gtksourceview package
- Remove bonobo*, not yet in releases

* Fri Aug 06 2004 Pascal Terjan <pterjan@mandrake.org> 0.10.0-0.20040805.1mdk
- New CVS Snapshot
- GStreamer is back
- Drop patch1 (merge upstream)

* Fri Jun 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.2-0.20040602.2mdk
- fix typo in tag name

* Thu Jun 03 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.2-0.20040602.1mdk
- CVS 20040602
- Remove TrayIcon, it's a separate project

* Wed May 12 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.2-0.20040509.2mdk
- Add missing Requires

* Mon May 10 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.2-0.20040509.1mdk
- CVS 20040509 + patchs applet/tray
- New packages : ruby-bonobo2 ruby-bonoboui2 ruby-panelapplet2
- Explicit list of files
- Rewrite descriptions
- Disable GStreamer as the binding is not yet ported to 0.8

* Sun Apr 11 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.1-1mdk
- 0.9.1
- Drop patch0

* Sun Mar 07 2004 Pascal Terjan <pterjan@mandrake.org> 0.9.0-1mdk
- 0.9.0
- Ruby/ATK added
- Updated patch0

