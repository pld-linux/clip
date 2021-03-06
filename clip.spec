#
# Conditional build:
%bcond_with	cobra
%bcond_with	codb
%bcond_with	bzip2
%bcond_without	com
%bcond_without	crypto
%bcond_with	cti
%bcond_with	gtk
%bcond_with	gd
%bcond_with	gtk2
%bcond_with	gzip
%bcond_with	mysql
%bcond_with	oasis
%bcond_with	odbc
%bcond_with	pgsql
%bcond_with	rtf
%bcond_with	fw
#
Summary:	XBASE/Clipper compatible program compiler
Summary(pl.UTF-8):	Kompilator programów kompatybilny z XBASE/Clipperem
Name:		clip
Version:	1.1.13
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.itk.ru/pub/clip/%{name}-prg-%{version}-1.tgz
# Source0-md5:	9debdcf2d879035b941ddc79850fde8d
#Source1:	patch.tgz
#Patch0:		clip-gtk2-windowgroupRemove.cis.patch
#Patch1:		clip-gtk2-transparent-EventBox.cis.patch
URL:		http://www.itk.ru/
%{?with_bzip2:BuildRequires:	bzip2-devel}
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	pam-devel
%{?with_gd:BuildRequires:	gd-devel}
%{?with_gtk:BuildRequires:	gtk+-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 1:2.0}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_crypto:BuildRequires:	openssl-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_gzip:BuildRequires:	zlib-devel}
Requires:	%{name}-lib = %{version}-%{release}
Requires:	binutils
Requires:	flex
Requires:	gcc
Requires:	gettext
Requires:	make
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		clipdir		%{_libdir}/clip
# XXX: build inside builddir
%define		tmpclipdir	%{_builddir}/clip-installed

%description
This package includes the clip compiler.

%description -l pl.UTF-8
Ten pakiet zawiera kompilator clip.

%package utils
# ??? the same as -lib? but different dep
Summary:	Utilities for CLIP
Summary(pl.UTF-8):	Narzędzia dla pakietu CLIP
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description utils
Utilities for CLIP.

%description utils -l pl.UTF-8
Narzędzia dla pakietu CLIP.

%package lib
Summary:	Runtime library for clip
Summary(pl.UTF-8):	Biblioteka uruchomieniowa dla pakietu clip
Group:		Libraries
# ??? not used
#PreReq:		/sbin/ldconfig
# ??? maybe -lib?
#Requires:	gpm

%description lib
This package provides runtime shared libraries for CLIP package.

%description lib -l pl.UTF-8
Ten pakiet dostarcza współdzielone biblioteki uruchomieniowe dla
pakietu CLIP.


%package cobra
Summary:	COBRA development for clip
Summary(pl.UTF-8):	Biblioteki COBRA dla pakietu clip
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description cobra
This package provides COBRA development for CLIP package

%description cobra -l pl.UTF-8
Ten pakiet dostarcza biblioteki COBRA dla pakietu clip.

%package codb
Summary:	CLIP object data base
Summary(pl.UTF-8):	Obiektowa baza danych CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description codb
This package provides CLIP object data base.

%description codb -l pl.UTF-8
Ten pakiet dostarcza obiektową bazę danych CLIP.

%package bzip2
Summary:	CLIP bzip2 binding
Summary(pl.UTF-8):	Wiązanie bzip2 dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	bzip2-libs

%description bzip2
This package provides bzip2 binding for CLIP.

%description bzip2 -l pl.UTF-8
Ten pakiet dostarcza wiązanie bzip2 dla pakiet CLIP.

%package com
Summary:	COM-port binding for CLIP
Summary(pl.UTF-8):	Wiązanie portu COM dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description com
This package provides COM-port binding for CLIP.

%description com -l pl.UTF-8
Wiązanie portu COM dla pakietu CLIP.

%package crypto
Summary:	CLIP cryptographic binding
Summary(pl.UTF-8):	Wiązanie kryptograficzne CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	openssl

%description crypto
This package provides cryptographic binding for CLIP.

%description crypto -l pl.UTF-8
Ten pakiet dostarcza wiązanie kryptograficzne dla pakietu CLIP.

%package cti
Summary:	CLIP cti binding
Summary(pl.UTF-8):	Wiązanie cti dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description cti
This package provides cti binding for CLIP.

%description cti -l pl.UTF-8
Ten pakiet dostarcza wiązanie cti dla pakietu CLIP.

%package gtk
Summary:	CLIP GTK+ binding
Summary(pl.UTF-8):	Wiązanie GTK+ dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	gtk+

%description gtk
This package provides GTK+ binding for CLIP.

%description gtk -l pl.UTF-8
Ten pakiet dostarcza wiązanie GTK+ dla pakietu CLIP.

%package gtk2
Summary:	CLIP GTK+2 binding
Summary(pl.UTF-8):	Wiązanie GTK+2 dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	gtk+2

%description gtk2
This package provides gtk2 binding for CLIP.

%description gtk2 -l pl.UTF-8
Ten pakiet dostarcza wiązanie GTK+2 dla pakietu CLIP.

%package gzip
Summary:	CLIP gzip binding
Summary(pl.UTF-8):	Wiązanie gzip dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	zlib

%description gzip
This package provides gzip binding for CLIP.

%description gzip -l pl.UTF-8
Ten pakiet dostarcza wiązanie gzip dla pakietu CLIP.

%package mysql
Summary:	CLIP MySQL binding
Summary(pl.UTF-8):	Wiązanie MySQL dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	mysql

%description mysql
This package provides MySQL binding for CLIP.

%description mysql -l pl.UTF-8
Ten pakiet dostarcza wiązanie MySQL dla pakietu CLIP.

%package oasis
Summary:	CLIP oasis binding
Summary(pl.UTF-8):	Wiązanie oasis dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description oasis
This package provides oasis binding for CLIP.

%description oasis -l pl.UTF-8
Ten pakiet dostarcza wiązanie oasis dla pakietu CLIP.

%package odbc
Summary:	CLIP ODBC binding
Summary(pl.UTF-8):	Wiązanie ODBC dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	unixODBC

%description odbc
This package provides ODBC binding for CLIP.

%description odbc -l pl.UTF-8
Ten pakiet dostarcza wiązanie ODBC dla pakietu CLIP.

%package postgres
Summary:	CLIP PostgreSQL binding
Summary(pl.UTF-8):	Wiązanie PostgreSQL dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	postgresql-libs

%description postgres
This package provides PostgreSQL binding for CLIP.

%description postgres -l pl.UTF-8
Ten pakiet dostarcza wiązanie PostgreSQL dla pakietu CLIP.

%package rtf
Summary:	CLIP RTF binding
Summary(pl.UTF-8):	Wiązanie RTF dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description rtf
This package provides RTF binding for CLIP.

%description rtf -l pl.UTF-8
Ten pakiet dostarcza wiązanie RTF dla pakietu CLIP.

%package gd
Summary:	CLIP gd binding
Summary(pl.UTF-8):	Wiązanie gd dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}
Requires:	gd

%description gd
This package provides gd binding for CLIP.

%description gd -l pl.UTF-8
Ten pakiet dostarcza wiązanie gd dla pakietu CLIP.

%package fw
Summary:	CLIP fw binding
Summary(pl.UTF-8):	Wiązanie fw dla pakietu CLIP
Group:		Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description fw
This package provides fw binding for CLIP.

%description fw -l pl.UTF-8
Ten pakiet dostarcza wiązanie fw dla pakietu CLIP.

%prep
%setup -q -n %{name}-prg-%{version}-1
#%patch0 -p1
#%patch1 -p1

#tar -xzf %{SOURCE1}
#cp -f -R clip-prg/* ./
#rm -f -R clip-prg

%build
install -d %{tmpclipdir}
export CLIPROOT=%{tmpclipdir}
mkdir -p $CLIPROOT
%{__make} local

%install
rm -rf $RPM_BUILD_ROOT
# XXX: FHS!
install -d $RPM_BUILD_ROOT%{clipdir}

# XXX: don't move, it breaks short-circuit
cp -r %{tmpclipdir}/bin			$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/cliprc		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/codb_ab		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/doc			$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/include		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/keymaps		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/lib			$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/locale.po	$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/term		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/charsets	$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/cobra		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/codb_abx	$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/etc			$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/kamache		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/lang		$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/locale.mo	$RPM_BUILD_ROOT%{clipdir}
cp -r %{tmpclipdir}/locale.pot	$RPM_BUILD_ROOT%{clipdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{clipdir}/bin/add_meta_tag
%attr(755,root,root) %{clipdir}/bin/clip
%attr(755,root,root) %{clipdir}/bin/clip_bug
%attr(755,root,root) %{clipdir}/bin/clip_conv
%attr(755,root,root) %{clipdir}/bin/clip_cp
%attr(755,root,root) %{clipdir}/bin/clip_dbg
%attr(755,root,root) %{clipdir}/bin/clip_hashextract
%attr(755,root,root) %{clipdir}/bin/clip_makelib
%attr(755,root,root) %{clipdir}/bin/clip_makeslib
%attr(755,root,root) %{clipdir}/bin/clip_msgfmt
%attr(755,root,root) %{clipdir}/bin/clip_msgmerge
%attr(755,root,root) %{clipdir}/bin/clip_trans
%attr(755,root,root) %{clipdir}/bin/clipar
%attr(755,root,root) %{clipdir}/bin/cliphash
%attr(755,root,root) %{clipdir}/bin/gen_tbl
%attr(755,root,root) %{clipdir}/bin/joinlib.sh
%attr(755,root,root) %{clipdir}/bin/lowname
%attr(755,root,root) %{clipdir}/bin/po_compat
%attr(755,root,root) %{clipdir}/bin/po_extr
%attr(755,root,root) %{clipdir}/bin/po_subst
%attr(755,root,root) %{clipdir}/bin/tconv
%attr(755,root,root) %{clipdir}/bin/xclip
%dir %{clipdir}/cliprc
%{clipdir}/cliprc/.notrm
%{clipdir}/cliprc/clipflags
%{clipdir}/doc/example/Makefile
%{clipdir}/doc/example/*.ch
%{clipdir}/doc/example/*.prg
%{clipdir}/doc/example/test.dbf.orig
%{clipdir}/include/Makefile.inc
%{clipdir}/include/Makefile.tdoc
%{clipdir}/include/_win32.h
%{clipdir}/include/achoice.ch
%{clipdir}/include/aof.ch
%{clipdir}/include/assert.ch
%{clipdir}/include/blob.ch
%{clipdir}/include/box.ch
%{clipdir}/include/browsys.ch
%{clipdir}/include/btree.h
%{clipdir}/include/button.ch
%{clipdir}/include/clip.ch
%{clipdir}/include/fwin/*
%{clipdir}/include/clip.h
#%{clipdir}/include/clipbase.h
%{clipdir}/include/clipbrd.ch
%{clipdir}/include/clipcfg.h
%{clipdir}/include/clipcfg.sh
%{clipdir}/include/clr_html.ch
%{clipdir}/include/color.ch
%{clipdir}/include/common.ch
%{clipdir}/include/config.ch
%{clipdir}/include/ct.ch
%{clipdir}/include/ctdisk.ch
%{clipdir}/include/ctdrv.ch
%{clipdir}/include/ctkbd.ch
%{clipdir}/include/ctmisc.ch
%{clipdir}/include/ctnnet.ch
%{clipdir}/include/ctppc.ch
%{clipdir}/include/ctprint.ch
%{clipdir}/include/ctps.ch
%{clipdir}/include/ctscan.ch
%{clipdir}/include/ctsys.ch
%{clipdir}/include/ctvideo.ch
%{clipdir}/include/ctwin.ch
%{clipdir}/include/date.ch
%{clipdir}/include/dbedit.ch
%{clipdir}/include/dbfsql.h
%{clipdir}/include/dbinames.ch
%{clipdir}/include/dbinfo.ch
%{clipdir}/include/dbms.ch
%{clipdir}/include/dbstruct.ch
%{clipdir}/include/debug.ch
%{clipdir}/include/directry.ch
%{clipdir}/include/edit.ch
%{clipdir}/include/error.ch
%{clipdir}/include/fileio.ch
%{clipdir}/include/form.ch
%{clipdir}/include/fox.ch
%{clipdir}/include/foxsql.ch
%{clipdir}/include/frmdef.ch
%{clipdir}/include/func_ref.ch
%{clipdir}/include/getexit.ch
%{clipdir}/include/hash.h
%{clipdir}/include/html.ch
%{clipdir}/include/imenu.ch
%{clipdir}/include/inkey.ch
%{clipdir}/include/key_name.ch
%{clipdir}/include/lang.ch
%{clipdir}/include/lbldef.ch
%{clipdir}/include/llibg.ch
%{clipdir}/include/memdebug
%{clipdir}/include/memoedit.ch
%{clipdir}/include/mset.ch
%{clipdir}/include/http.ch
%{clipdir}/include/ord.ch
%{clipdir}/include/ordinfo.ch
%{clipdir}/include/pgch.ch
%{clipdir}/include/rdd.ch
%{clipdir}/include/rddsys.ch
%{clipdir}/include/reserved.ch
%{clipdir}/include/set.ch
%{clipdir}/include/setcurs.ch
%{clipdir}/include/setnames.ch
%{clipdir}/include/simpleio.ch
%{clipdir}/include/six.ch
%{clipdir}/include/six2clip.ch
%{clipdir}/include/std.ch
%{clipdir}/include/std50.ch
%{clipdir}/include/std53.ch
%{clipdir}/include/task.h
%{clipdir}/include/taskcfg.h
%{clipdir}/include/tbrowse.ch
%{clipdir}/include/ulimit.ch
%{clipdir}/lib/libclip.a
%{clipdir}/lib/libclip.ex
%{clipdir}/lib/libclip.nm
%{clipdir}/include/pp_harb.ch
%{clipdir}/include/ppclass.ch
%{clipdir}/include/rp_dot.ch
%{clipdir}/include/rp_run.ch
%{clipdir}/include/bggraph.ch
# XXX: missing dirs below!
# 
%{clipdir}/locale.mo/*/clip-cti.mo
%{clipdir}/locale.mo/*/clip-fw.mo
#%{clipdir}/locale.mo/*/clip-gtk2.mo
%{clipdir}/locale.mo/*/clip-r2d2.mo
%{clipdir}/locale.mo/*/mod-ini.mo
%{clipdir}/locale.mo/*/clip.mo
%{clipdir}/locale.mo/*/cliprt.mo
%{clipdir}/locale.po/*/clip.po
%{clipdir}/locale.po/*/cliprt.po

%{clipdir}/locale.mo/*/sys.mo
%{clipdir}/locale.po/*/sys.po
%{clipdir}/locale.pot/sys/*

%{clipdir}/locale.mo/*/debug.mo
%{clipdir}/locale.po/*/debug.po
%{clipdir}/locale.pot/debug/*

%{clipdir}/locale.po/*/brow.po
%{clipdir}/locale.mo/*/brow.mo
%{clipdir}/locale.po/*/ca_dbu.po
%{clipdir}/locale.mo/*/ca_dbu.mo

%{clipdir}/locale.po/*/pp.po
%{clipdir}/locale.mo/*/pp.mo
#%{clipdir}/locale.pot/pp/*

%{clipdir}/locale.po/*/udb.po
%{clipdir}/locale.mo/*/udb.mo
%{clipdir}/locale.pot/udb/*

#%{clipdir}/locale.pot/udbx/*.pot
%{clipdir}/locale.po/*/udbx.po
%{clipdir}/locale.mo/*/udbx.mo

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{clipdir}/bin/bdbf*
%attr(755,root,root) %{clipdir}/bin/clip_bl
%attr(755,root,root) %{clipdir}/bin/clip_blank
%attr(755,root,root) %{clipdir}/bin/clip_cld
%attr(755,root,root) %{clipdir}/bin/clip_dbf2txt
%attr(755,root,root) %{clipdir}/bin/clip_fl
%attr(755,root,root) %{clipdir}/bin/clip_hindex
%attr(755,root,root) %{clipdir}/bin/clip_hseek
%attr(755,root,root) %{clipdir}/bin/clip_hv
%attr(755,root,root) %{clipdir}/bin/clip_prg
%attr(755,root,root) %{clipdir}/bin/clip_run
%attr(755,root,root) %{clipdir}/bin/clip_we
%attr(755,root,root) %{clipdir}/bin/ctosgml
%attr(755,root,root) %{clipdir}/bin/dbc
%attr(755,root,root) %{clipdir}/bin/ftosgml
%attr(755,root,root) %{clipdir}/bin/pp_ron
%attr(755,root,root) %{clipdir}/bin/sqlrun
%attr(755,root,root) %{clipdir}/bin/wcl2prg
%attr(755,root,root) %{clipdir}/bin/www_clip
%{clipdir}/etc/.macro
%{clipdir}/etc/.templ
%{clipdir}/locale.pot/bdbfs/*.pot
%{clipdir}/locale.po/*/bdbfs.po
%{clipdir}/locale.mo/*/bdbfs.mo

%files lib
%defattr(644,root,root,755)
%dir %{clipdir}
%dir %{clipdir}/bin
%dir %{clipdir}/charsets
%{clipdir}/charsets/*
%dir %{clipdir}/doc
%dir %{clipdir}/doc/example
%dir %{clipdir}/etc
%{clipdir}/etc/environment
%{clipdir}/etc/printers.ini
%{clipdir}/etc/termcap
%{clipdir}/etc/terminfo/*/*
%dir %{clipdir}/include
%dir %{clipdir}/keymaps
%{clipdir}/keymaps/*
%dir %{clipdir}/lang
%{clipdir}/lang/*
%dir %{clipdir}/lib
%attr(755,root,root) %{clipdir}/lib/libclip.so
%dir %{clipdir}/locale.pot
%dir %{clipdir}/locale.po
%dir %{clipdir}/locale.mo
%dir %{clipdir}/term
%{clipdir}/term/*

%if %{with cobra}
%files cobra
%defattr(644,root,root,755)
%attr(755,root,root) %{clipdir}/bin/cobra_clnt1
%attr(755,root,root) %{clipdir}/bin/cobra_serv
%{clipdir}/cobra/auth/*
%{clipdir}/cobra/cobra*
%{clipdir}/cobra/*.po
%{clipdir}/cobra/files/*
%{clipdir}/cobra/tcp-wrap/*
%{clipdir}/include/cobra.ch
%{clipdir}/locale.pot/cobra_clnt/*
%{clipdir}/locale.pot/cobra_serv/*
%{clipdir}/locale.mo/*/cobra*
%{clipdir}/locale.po/*/cobra*
%endif

%if %{with codb}
%files codb
%defattr(644,root,root,755)
%attr(755,root,root) %{clipdir}/bin/codb_*
%{clipdir}/lib/libclip-codb.*
%dir %{clipdir}/codb_ab
%{clipdir}/codb_ab/plugins
%{clipdir}/codb_ab/reports
%dir %{clipdir}/codb_abx
%{clipdir}/codb_abx/plugins
%{clipdir}/include/codb.ch
%{clipdir}/include/codbcfg.ch
%lang(ru) %{clipdir}/locale.po/ru_RU.KOI8-R/codb.po
%{clipdir}/locale.pot/codb
%{clipdir}/locale.mo/*/codb.mo
%lang(es) %{clipdir}/locale.po/es_*/codb.po
%endif

%if %{with bzip2}
%files bzip2
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-bzip2
%{clipdir}/lib/libclip-bzip2.*
%endif

%if %{with com}
%files com
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-com
%{clipdir}/doc/clip-com
%{clipdir}/lib/libclip-com.*
%endif

%if %{with crypto}
%files crypto
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-crypto
%{clipdir}/lib/libclip-crypto.*
%endif

%if %{with cti}
%files cti
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-cti
%{clipdir}/etc/.calendar
%{clipdir}/include/cti.ch
%{clipdir}/include/cti
%{clipdir}/lib/libclip-cti.*
#%{clipdir}/locale.mo/*/clip-cti.mo
#%{clipdir}/locale.po/*/clip-cti.po
#%{clipdir}/locale.pot/clip-cti/*.pot
%endif

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
#%{clipdir}/cliprc/clip-gtk.cliprc
#%{clipdir}/doc/example/clip-gtk
#%{clipdir}/include/clip-gtk.ch
#%{clipdir}/include/clip-gtk.h
#%{clipdir}/lib/libclip-gtk.*
#%{clipdir}/locale.mo/*/clip-gtk.mo
#%{clipdir}/locale.po/*/clip-gtk.po
#%{clipdir}/locale.pot/clip-gtk/*
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%{clipdir}/cliprc/clip-gtk2.cliprc
%{clipdir}/doc/example/clip-gtk2
%{clipdir}/include/clip-gtk2.ch
%{clipdir}/include/clip-gtk2.h
%{clipdir}/include/gtk2-stock.ch
%{clipdir}/lib/libclip-gtk2.*
#%{clipdir}/locale.mo/*/clip-gtk2.mo
#%{clipdir}/locale.po/*/clip-gtk2.po
#%{clipdir}/locale.pot/clip-gtk2/*
%endif

%if %{with gzip}
%files gzip
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-gzip
%{clipdir}/lib/libclip-gzip.*
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-mysql
%{clipdir}/doc/clip-mysql
%{clipdir}/include/mysql.ch
%{clipdir}/lib/libclip-mysql.*
%endif

%if %{with oasis}
%files oasis
%defattr(644,root,root,755)
%{clipdir}/include/nanfor
%{clipdir}/include/netto
%{clipdir}/lib/libclip-nanfor.*
%{clipdir}/lib/libclip-netto.*
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%{clipdir}/lib/libclip-odbc.*
%endif

%if %{with pgsql}
%files postgres
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-postgres
%{clipdir}/doc/clip-postgres
%{clipdir}/include/postgres.ch
%{clipdir}/lib/libclip-postgres.*
%endif

%if %{with rtf}
%files rtf
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-rtf
%{clipdir}/include/objects.ch
%{clipdir}/include/richtext.ch
%{clipdir}/lib/libclip-rtf.*
%endif

%if %{with gd}
%files gd
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-gd
%{clipdir}/doc/clip-gd
%{clipdir}/include/gdinfo.ch
%{clipdir}/lib/libclip-gd.*
%{clipdir}/lib/libgd.*
%endif

%if %{with fw}
%files fw
%defattr(644,root,root,755)
%{clipdir}/doc/example/clip-fw
%{clipdir}/lib/libclip-fw.*
#%{clipdir}/locale.mo/*/clip-fw.mo
#%{clipdir}/locale.po/*/clip-fw.po
#%{clipdir}/locale.pot/clip-fw/*
%endif
