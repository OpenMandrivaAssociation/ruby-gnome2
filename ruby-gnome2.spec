%define name ruby-gnome2
%define version 0.16.0
%define release %mkrel 4
%define rubyver 1.8

Summary: Set of Ruby language bindings for the GNOME 2.0
Name: %name
Version: %version
Release: %release
License: LGPL
Group: Development/Ruby
URL: http://ruby-gnome2.sourceforge.jp/
Source0: http://ovh.dl.sourceforge.net/sourceforge/ruby-gnome2/%{name}-all-%{version}.tar.bz2
Patch0:	ruby-gnome2-0.16.0-libglade_nil_check.patch
Patch1:	ruby-gnome2-0.16.0-gtk_warning.patch
Patch2:	ruby-gnome2-0.16.0-timeout_add_seconds.patch
Patch3:	ruby-gnome2-0.16.0-rbgtk_register_treeiter_set_value_func.patch
Patch4:	ruby-gnome2-0.16.0-rbgobj_boxed_get.patch
Patch5:	ruby-gnome2-0.16.0-G_TYPE_UNICODE_SCRIPT_TYPE.patch
Patch6:	ruby-gnome2-0.16.0-poppler.patch
Patch7:	ruby-gnome2-0.16.0-CVE-2007-6183.patch
Patch8:	ruby-gnome2-0.16.0-glib2.0-2.15.5-fix-mkenums.patch
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: ruby-devel libGConf2-devel libgnomeui2-devel
BuildRequires: libgnomecanvas2-devel libart_lgpl-devel > 2 png-devel
BuildRequires: gtk+2-devel pango-devel libgdk_pixbuf2.0-devel
BuildRequires: atk-devel glib2-devel gnome-vfs2-devel
BuildRequires: libgtkhtml2-devel > 2.4 gtkglext-devel 
BuildRequires: gda2.0-devel >= 1.0.2
BuildRequires: libglade2.0-devel libpanel-applet-2-devel
BuildRequires: gtksourceview1-devel >= 1.0.1
BuildRequires: librsvg-devel >= 2.8.0
BuildRequires: libgnomeprintui-devel >= 2.8.0 libgnomeprint-devel >= 2.6.0
BuildRequires: libvte-devel
BuildRequires: libpoppler-devel libpoppler-glib-devel
BuildRequires: libmozilla-firefox-devel

Requires: ruby >= %{rubyver}
Requires: ruby-libart2 = %version
Requires: ruby-gtk2 = %version
Requires: ruby-gnomecanvas2 = %version

%description
set of Ruby language bindings for the GNOME 2.0 development environment. This
is the next generation of Ruby-GNOME.

%package devel
Summary: Headers for developing with Ruby/Gnome2, Ruby/Gtk2, 
License: LGPL
Group: Development/Ruby
Requires: %name = %version
Obsoletes: ruby-gtk2-devel
Provides: ruby-gtk2-devel

%description devel
Ruby bindings for Gnome2.
This package contains header files needed for developing Ruby extensions
depending on Ruby/Gnome2, Ruby/Glib2, Ruby/Pango, ...

%package -n ruby-glib2
Summary: Ruby binding of GLib-2.x
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-glib2
Ruby/GLib2 is a Ruby binding of GLib-2.x.

%package -n ruby-gtk2
Summary: Ruby binding of GTK+2.0.x
Group: Development/Ruby
Requires: ruby-atk = %version
Requires: ruby-pango = %version
Requires: ruby-gdkpixbuf2 = %version

%description -n ruby-gtk2
Ruby/GTK2 is a Ruby binding of GTK+2.0.x.

%package -n ruby-gdkpixbuf2
Summary: Ruby binding of GdkPixbuf-2.x
Group: Development/Ruby
Requires: ruby-glib2 = %version
Requires: ruby-gtk2 = %version

%description -n ruby-gdkpixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%package -n ruby-atk
Summary: Ruby binding of ATK-1.0.x or later
Group: Development/Ruby
Requires: ruby-glib2 = %version

%description -n ruby-atk
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.

%package -n ruby-pango
Summary: Ruby binding of pango-1.x
Group: Development/Ruby
Requires: ruby-glib2 = %version

%description -n ruby-pango
Ruby/Pango is a Ruby binding of pango-1.x.

%package -n ruby-libglade2
Summary: Ruby bindings of Libglade2
Group: Development/Ruby
Requires: ruby-gtk2 = %version

%description -n ruby-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby-libart2
Summary: Ruby binding of Libart_lgpl
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl.

%package -n ruby-gnomecanvas2
Summary: Ruby binding of GnomeCanvas-2.x
Group: Development/Ruby
Requires: ruby-libart2 = %version
Requires: ruby-gtk2 = %version

%description -n ruby-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby-gconf2
Summary: Ruby binding of GConf-1.2.x
Group: Development/Ruby
Requires: ruby-glib2 = %version

%description -n ruby-gconf2
Ruby/GConf2 is a Ruby binding of GConf-1.2.x.

%package -n ruby-gnomevfs2
Summary: Ruby binding of GnomeVFS-2.0.x
Group: Development/Ruby
Requires: ruby-glib2 = %version ruby-gconf2 = %version

%description -n ruby-gnomevfs2
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby-gtkhtml2
Summary: Ruby binding of GtkHtml2
Group: Development/Ruby
Requires: ruby-gtk2 = %version

%description -n ruby-gtkhtml2
Ruby/GtkHtml2 is a Ruby binding of GtkHtml2.

%package -n ruby-gtkglext
Summary: Ruby binding of GtkGLExt
Group: Development/Ruby
Requires: ruby-rbogl
Requires: ruby-gtk2 = %version

%description -n ruby-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby-panelapplet2
Summary: Ruby binding of libpanel-applet-2.x
Group: Development/Ruby
Requires: ruby-glib2 = %version
Requires: ruby-gtk2 = %version

%description -n ruby-panelapplet2
Ruby/PanelApplet2 is a Ruby binding of libpanel-applet-2.x.

%package -n ruby-gtksourceview
Summary: Ruby binding of gtksourceview-1.0.x
Group: Development/Ruby
Requires: ruby-gtk2 = %version

%description -n ruby-gtksourceview
Ruby/GtkSourceView is a Ruby binding of gtksourceview-1.0.x.

%package -n ruby-gnomeprint2
Summary: Ruby binding of libgnomeprint
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-gnomeprint2
Ruby/GnomePrint is a Ruby binding of libgnomeprint.

%package -n ruby-gnomeprintui2
Summary: Ruby binding of libgnomeprintui
Group: Development/Ruby
Requires: ruby-gtk2 = %version

%description -n ruby-gnomeprintui2
Ruby/GnomePrintUI is a Ruby binding of libgnomeprintui.

%package -n ruby-rsvg2
Summary: Ruby binding of librsvg
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-rsvg2
Ruby/RSVG is a Ruby binding of librsvg.

%package -n ruby-vte
Summary: Ruby binding of libvte
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-vte
Ruby/VTE is a Ruby binding of libvte.

%package -n ruby-poppler
Summary: Ruby binding of poppler-glib
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-poppler
Ruby/Poppler is a Ruby binding of poppler-glib.

%package -n ruby-gtkmozembed
Summary: Ruby binding of GtkMozEmbed
Group: Development/Ruby
Requires: ruby >= %{rubyver}

%description -n ruby-gtkmozembed
Ruby/GtkMozEmbed is a Ruby binding of GtkMozEmbed a widget embedding a
Mozilla Gecko renderer.


%prep 
%setup -q -n ruby-gnome2-all-%version
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p1 -b .cve-2007-6183
%patch8 -p1

%build
ruby extconf.rb
%make

find */* -name \*.rb -exec sed -i -e 's|/usr/local/bin/ruby|/usr/bin/ruby|' {} \;

%install
rm -rf %buildroot
make install DESTDIR=%buildroot libdir=%buildroot%{_libdir} archdir=%buildroot%ruby_sitearchdir

mkdir -p %buildroot%{_bindir}
cp libglade/bin/* %buildroot%{_bindir}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -n ruby-glib2
%defattr(-,root,root)
%{ruby_sitearchdir}/glib2.so
%{ruby_sitelibdir}/glib2.rb
%{ruby_sitelibdir}/glib-mkenums.rb
%doc AUTHORS glib/{COPYING.LIB,ChangeLog,README}

%files -n ruby-gtk2
%defattr(-,root,root)
%{ruby_sitearchdir}/gtk2.so
%{ruby_sitelibdir}/gtk2.rb
%{ruby_sitelibdir}/gtk2/base.rb
%doc AUTHORS gtk/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-gdkpixbuf2
%defattr(-,root,root)
%{ruby_sitearchdir}/gdk_pixbuf2.so
%{ruby_sitelibdir}/gdk_pixbuf2.rb
%doc AUTHORS gdkpixbuf/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-panelapplet2
%defattr(-,root,root)
%{ruby_sitearchdir}/panelapplet2.so
%{ruby_sitelibdir}/panelapplet2.rb
%doc AUTHORS panel-applet/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-pango
%defattr(-,root,root)
%{ruby_sitearchdir}/pango.so
%{ruby_sitelibdir}/pango.rb
%doc AUTHORS pango/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-libglade2
%defattr(-,root,root)
%{ruby_sitearchdir}/libglade2.so
%{ruby_sitelibdir}/libglade2.rb
/usr/bin/ruby-glade-create-template
%doc AUTHORS libglade/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-libart2
%defattr(-,root,root)
%{ruby_sitearchdir}/libart2.so
%doc AUTHORS libart/{COPYING.LIB,ChangeLog,README,sample}

%files
%defattr(-,root,root)
%{ruby_sitearchdir}/gnome2.so
%{ruby_sitelibdir}/gnome2.rb
%doc AUTHORS gnome/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-gnomecanvas2
%defattr(-,root,root)
%{ruby_sitearchdir}/gnomecanvas2.so
%{ruby_sitelibdir}/gnomecanvas2.rb
%doc AUTHORS gnomecanvas/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-gconf2
%defattr(-,root,root)
%{ruby_sitearchdir}/gconf2.so
%{ruby_sitelibdir}/gconf2.rb
%doc AUTHORS gconf/{COPYING.LIB,ChangeLog,README,tests}

%files -n ruby-gnomevfs2
%defattr(-,root,root)
%{ruby_sitearchdir}/gnomevfs.so
%{ruby_sitelibdir}/gnomevfs.rb
%doc AUTHORS gnomevfs/{COPYING.LIB,ChangeLog,README,tests}

%files -n ruby-gtkhtml2
%defattr(-,root,root)
%{ruby_sitearchdir}/gtkhtml2.so
%{ruby_sitelibdir}/gtkhtml2.rb
%doc AUTHORS gtkhtml2/{COPYING.LIB,ChangeLog,README,sample}

%files -n ruby-gtkglext
%defattr(-,root,root)
%{ruby_sitearchdir}/gtkglext.so
%{ruby_sitelibdir}/gtkglext.rb
%doc AUTHORS gtkglext/{ChangeLog,README,sample}

%files -n ruby-atk
%defattr(-,root,root)
%{ruby_sitearchdir}/atk.so
%{ruby_sitelibdir}/atk.rb
%doc AUTHORS atk/{COPYING.LIB,ChangeLog,README}

%files -n ruby-gtksourceview
%defattr(-,root,root)
%{ruby_sitearchdir}/gtksourceview.so
%{ruby_sitelibdir}/gtksourceview.rb
%doc AUTHORS gtksourceview/{ChangeLog,README,sample,COPYING.LIB}

%files -n ruby-gnomeprint2
%defattr(-,root,root)
%{ruby_sitearchdir}/gnomeprint2.so
%{ruby_sitelibdir}/gnomeprint2.rb
%doc AUTHORS gnomeprint/{COPYING.LIB,ChangeLog,README,sample,test}

%files -n ruby-gnomeprintui2
%defattr(-,root,root)
%{ruby_sitearchdir}/gnomeprintui2.so
%{ruby_sitelibdir}/gnomeprintui2.rb
%doc AUTHORS gnomeprintui/{ChangeLog,README,sample,COPYING.LIB}

%files -n ruby-rsvg2
%defattr(-,root,root)
%{ruby_sitearchdir}/rsvg2.so
%{ruby_sitelibdir}/rsvg2.rb
%doc AUTHORS rsvg/{ChangeLog,README,sample,COPYING.LIB}

%files -n ruby-vte
%defattr(-,root,root)
%{ruby_sitearchdir}/vte.so
%{ruby_sitelibdir}/vte.rb
%doc AUTHORS vte/{ChangeLog,README,sample,COPYING.LIB}

%files -n ruby-poppler
%defattr(-,root,root)
%{ruby_sitearchdir}/poppler.so
%{ruby_sitelibdir}/poppler.rb
%doc AUTHORS poppler/{ChangeLog,README,sample,COPYING.LIB}

%files -n ruby-gtkmozembed
%defattr(-,root,root)
%{ruby_sitearchdir}/gtkmozembed.so
%{ruby_sitelibdir}/gtkmozembed.rb
%doc AUTHORS gtkmozembed/{ChangeLog,README,sample,COPYING.LIB}

%files devel
%defattr(-,root,root)
%{ruby_sitelibdir}/mkmf-gnome2.rb
%{ruby_sitelibdir}/pkg-config.rb
%{ruby_sitearchdir}/*.h

