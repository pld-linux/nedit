Summary:	Motif/X Window GUI editor
Summary(pl):    graficzny edytor dla Motif/X Window
Name:		nedit
Version:	5.0.2
Release:	2
Source0:	ftp://ftp.fnal.gov/pub/nedit/5_0_2/nedit_source.tar.gz
Source1:	nedit.wmconfig
Copyright:	distributable
Group:		Applications/Editors
Group(pl):      Aplikacje/Edytory
URL:		http://www-pat.fnal.gov/nirvana/nedit.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
NEdit is a GUI style plain-text editor for X/Motif systems. 
It is very easy to use, especially for those familiar 
with the Macintosh or MS Windows style of interface, combining 
full use of the mouse and window manager, with keystroke efficiency and a 
full complement of powerful editing commands. 

%description -l pl
NEdit to tekstowy edytor o graficznym interfejsie dla systemów X/Motif.
Jest bardzo prosty w u¿yciu, zw³aszcza dla osób zaznajomionych
z interfejsami w stylu Macintosha czy MS Windows. £±czy w sobie pe³ne
wykorzystanie myszy i zarz±dcy okien z wydajno¶ci± klawiatury, 
a ca³o¶ci dope³nienia ca³a gama potê¿nych poleceñ edycyjnych.

%prep
%setup -q -c -n nedit

%build
make linux_nedit \
	CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -DUSE_DIRENT \
	-DUSE_LPR_PRINT_CMD"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/X11R6/{bin,man/man1},etc/X11/wmconfig}
install -s source/{nedit,nc} $RPM_BUILD_ROOT/usr/X11R6/bin
install nedit.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/nedit.1x
install nc.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/nc.1x
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/nedit

gzip -9nf nedit.doc README \
	$RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc nedit.doc.gz README.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*

%config(missingok) /etc/X11/wmconfig/nedit
