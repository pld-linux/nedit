Summary:   Motif/X windows GUI editor
Name:      nedit
Version:   5.02
Release:   1
Source:    ftp://ftp.fnal.gov/pub/nedit/5_0_2/nedit_source.tar.gz
Copyright: distributable
Group:     Applications/Editors
URL:       http://www-pat.fnal.gov/nirvana/nedit.html
Buildroot: /tmp/%{name}-%{version}-root

%description
NEdit is a GUI style plain-text editor for X/Motif systems. 
It is very easy to use, especially for those familiar 
with the Macintosh or MS Windows style of interface, combining 
full use of the mouse and window manager, with keystroke efficiency and a 
full complement of powerful editing commands. 

%prep
%setup -q -c -n nedit

%build
make linux_nedit \
	CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -DUSE_DIRENT \
	-DUSE_LPR_PRINT_CMD"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install -s source/{nedit,nc} $RPM_BUILD_ROOT/usr/X11R6/bin
install nedit.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/nedit.1x
install nc.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/nc.1x

%files
%attr(644, root, root, 755) %doc nedit.doc README
%attr(644, root,  man) /usr/X11R6/man/man1/*
%attr(755, root, root) /usr/X11R6/bin/*

%changelog
* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.02-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files.

* Sat Mar 07 1998 Troy Benjegedes <troybenj@iastate.edu>
- Updated to nedit 5.01 (crashing bugfixes for Linux)

* Wed Jul 23 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- all rewrited for using Buildroot,
- removed %ifarch from %prep; removed paching source,
- nedit is dynamically linked with lesstif,
- removed "ExclusiveArch: i386",
- added %attr macros in %files (allow build package from non root account).
