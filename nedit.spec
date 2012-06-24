Summary:	Motif/X Window GUI editor
Summary(pl):    Edytor tekstu  Motif/X Window
Name:		nedit
Version:	5.0.2
Release:	4
Source0:	ftp://ftp.fnal.gov/pub/nedit/5_0_2/nedit_source.tar.gz
Source1:	nedit.desktop
Copyright:	distributable
Group:		Applications/Editors
Group(pl):      Aplikacje/Edytory
URL:		http://www-pat.fnal.gov/nirvana/nedit.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
NEdit is a GUI style plain-text editor for X/Motif systems. 
It is very easy to use, especially for those familiar 
with the Macintosh or MS Windows style of interface, combining 
full use of the mouse and window manager, with keystroke efficiency and a 
full complement of powerful editing commands. 

%description -l pl
NEdit to edytor tekstu o graficznym interfejsie dla system�w X/Motif.
Jest bardzo prosty w u�yciu, zw�aszcza dla os�b zaznajomionych
z interfejsami w stylu Macintosha czy MS Windows. ��czy w sobie pe�ne
wykorzystanie myszy i zarz�dcy okien z wydajno�ci� klawiatury, 
a ca�o�ci dope�nienia ca�a gama pot�nych polece� edycyjnych.

%prep
%setup -q -c -n nedit

%build
make linux_nedit \
	CFLAGS="$RPM_OPT_FLAGS -I%{_includedir} -DUSE_DIRENT \
	-DUSE_LPR_PRINT_CMD"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_applnkdir}/Office/Editors}

install -s source/{nedit,nc} $RPM_BUILD_ROOT%{_bindir}
install nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
install nc.man $RPM_BUILD_ROOT%{_mandir}/man1/nc.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors

gzip -9nf nedit.doc README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc nedit.doc.gz README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%{_applnkdir}/Office/Editors/nedit.desktop
