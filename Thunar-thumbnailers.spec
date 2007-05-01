#
%define		srcname	thunar-thumbnailers
#
Summary:	Thumbnailers plugin for the Thunar file manager
Summary(pl):	Wtyczka Thumbnailers dla zarz±dcy plików Thunar
Name:		Thunar-thumbnailers
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/thunar-thumbnailers/%{srcname}-%{version}.tar.bz2
# Source0-md5:	9d1e5ebe36c8672048062392d4f329b9
Patch0:		%{name}-configure.patch
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-thumbnailers
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	shared-mime-info
Requires:	Thunar >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunar-thumbnailers provides additional thumbnailers for use by the
Thunar file manager.

%description -l pl
Thunar-thumbnailers dostarcza dodatkowe modu³y wykonuj±ce miniaturki
plików dla zarz±dcy plików Thunar.

%prep
%setup -q -n %{srcname}-0.0.1svn-r02578
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-raw \
	--enable-tex \
	--enable-grace \
	--enable-ffmpeg \
	--disable-update-mime-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%banner %{name} -e << EOF
For full functionality, you need to install:
- ImageMagick
- dcraw
- ffmpegthumbnailer
- grace
- tetex-format-latex
EOF

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/agr-thumbnailer
%attr(755,root,root) %{_libdir}/eps-thumbnailer
%attr(755,root,root) %{_libdir}/ffmpeg-thumbnailer
%attr(755,root,root) %{_libdir}/fig-thumbnailer
%attr(755,root,root) %{_libdir}/ps-thumbnailer
%attr(755,root,root) %{_libdir}/raw-thumbnailer
%attr(755,root,root) %{_libdir}/tex-thumbnailer
%{_datadir}/mime/packages/thunar-thumbnailers.xml
%{_datadir}/thumbnailers/agr-thumbnailer.desktop
%{_datadir}/thumbnailers/eps-thumbnailer.desktop
%{_datadir}/thumbnailers/ffmpeg-thumbnailer.desktop
%{_datadir}/thumbnailers/fig-thumbnailer.desktop
%{_datadir}/thumbnailers/ps-thumbnailer.desktop
%{_datadir}/thumbnailers/raw-thumbnailer.desktop
%{_datadir}/thumbnailers/tex-thumbnailer.desktop
