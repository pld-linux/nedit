Summary:	Motif/X Window GUI editor
Summary(pl):	Edytor tekstu  Motif/X Window
Name:		nedit
Version:	5.2
Release:	1
License:	GPL v2
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	ftp://ftp.nedit.org/pub/v5_1_1/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://nedit.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	lesstif-devel >= 0.89.4

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
NEdit is a GUI style plain-text editor for X/Motif systems. It is very
easy to use, especially for those familiar with the Macintosh or MS
Windows style of interface, combining full use of the mouse and window
manager, with keystroke efficiency and a full complement of powerful
editing commands.

%description -l pl
NEdit to edytor tekstu o graficznym interfejsie dla systemów X/Motif.
Jest bardzo prosty w u¿yciu, zw³aszcza dla osób zaznajomionych z
interfejsami w stylu Macintosha czy MS Windows. £±czy w sobie pe³ne
wykorzystanie myszy i zarz±dcy okien z wydajno¶ci± klawiatury, a
ca³o¶ci dope³nienia ca³a gama potê¿nych poleceñ edycyjnych.

%prep
%setup -q 

%build
%{__make} linux \
	CFLAGS="%{rpmcflags} -I%{_includedir} -DUSE_DIRENT \
	-DUSE_LPR_PRINT_CMD"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_applnkdir}/Office/Editors,%{_pixmapsdir}}

install source/{nedit,nc} $RPM_BUILD_ROOT%{_bindir}
install doc/nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
install doc/nc.man $RPM_BUILD_ROOT%{_mandir}/man1/nc.1x

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf doc/nedit.doc README ReleaseNotes ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Office/Editors/nedit.desktop
%{_pixmapsdir}/*
