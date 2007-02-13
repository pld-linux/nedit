# TODO
# - menu Shell items require csh, remove that dependency
Summary:	Motif/X Window GUI editor
Summary(pl.UTF-8):	Edytor tekstu z interfejsem graficznym Motif/X Window
Name:		nedit
Version:	5.5
Release:	2
License:	GPL v2
Group:		Applications/Editors
Source0:	ftp://ftp.nedit.org/pub/NEdit/v5_5/%{name}-%{version}-src.tar.bz2
# Source0-md5:	48cb3dce52d44988f3a4d7c6f47b6bbe
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-security.patch
Patch1:		%{name}-dynamic-motif.patch
URL:		http://nedit.org/
BuildRequires:	motif-devel >= 1.2
Requires:	/bin/csh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NEdit is a GUI style plain-text editor for X/Motif systems. It is very
easy to use, especially for those familiar with the Macintosh or MS
Windows style of interface, combining full use of the mouse and window
manager, with keystroke efficiency and a full complement of powerful
editing commands.

%description -l pl.UTF-8
NEdit to edytor tekstu o graficznym interfejsie dla systemów X/Motif.
Jest bardzo prosty w użyciu, zwłaszcza dla osób zaznajomionych z
interfejsami w stylu Macintosha czy MS Windows. Łączy w sobie pełne
wykorzystanie myszy i zarządcy okien z wydajnością klawiatury, a
całości dopełnienia cała gama potężnych poleceń edycyjnych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
echo | %{__make} linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUSE_DIRENT -DUSE_LPR_PRINT_CMD -DBUILD_UNTESTED_NEDIT -DBUILD_BROKEN_NEDIT" \
	LXLIB="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

install source/nedit $RPM_BUILD_ROOT%{_bindir}
install source/nc $RPM_BUILD_ROOT%{_bindir}/nclient
install doc/nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
install doc/nc.man $RPM_BUILD_ROOT%{_mandir}/man1/nclient.1x

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/nedit.doc README ReleaseNotes ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/nedit.desktop
%{_pixmapsdir}/*.png
