#
%define		srcname	thunar-thumbnailers
#
Summary:	Thumbnailers plugin for the Thunar file manager
Summary(pl.UTF-8):	Wtyczka Thumbnailers dla zarządcy plików Thunar
Name:		Thunar-thumbnailers
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/thunar-thumbnailers/%{srcname}-%{version}.tar.bz2
# Source0-md5:	b451516fcfa97c8fabf71cf935a2550a
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-thumbnailers
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dcraw
BuildRequires:	grace
BuildRequires:	raw-thumbnailer
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tetex-format-latex
Requires(post,postun):	shared-mime-info
Requires:	Thunar >= 0.8.0
Suggests:	ImageMagick
Suggests:	dcraw
Suggests:	ffmpegthumbnailer
Suggests:	grace
Suggests:	raw-thumbnailer
Suggests:	tetex-format-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunar-thumbnailers provides additional thumbnailers for use by the
Thunar file manager.

%description -l pl.UTF-8
Thunar-thumbnailers dostarcza dodatkowe moduły wykonujące miniaturki
plików dla zarządcy plików Thunar.

%prep
%setup -q -n thunar-thumbnailers-%{version}

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

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/agr-thumbnailer
%attr(755,root,root) %{_libdir}/dvi-thumbnailer
%attr(755,root,root) %{_libdir}/eps-thumbnailer
%attr(755,root,root) %{_libdir}/ffmpeg-thumbnailer
%attr(755,root,root) %{_libdir}/fig-thumbnailer
%attr(755,root,root) %{_libdir}/odf-thumbnailer
%attr(755,root,root) %{_libdir}/ogg-thumbnailer
%attr(755,root,root) %{_libdir}/pdf-thumbnailer
%attr(755,root,root) %{_libdir}/ps-thumbnailer
%attr(755,root,root) %{_libdir}/raw-thumbnailer
%attr(755,root,root) %{_libdir}/svgz-thumbnailer
%attr(755,root,root) %{_libdir}/tex-thumbnailer
%{_datadir}/mime/packages/thunar-thumbnailers.xml
%{_datadir}/thumbnailers/agr-thumbnailer.desktop
%{_datadir}/thumbnailers/dvi-thumbnailer.desktop
%{_datadir}/thumbnailers/eps-thumbnailer.desktop
%{_datadir}/thumbnailers/ffmpeg-thumbnailer.desktop
%{_datadir}/thumbnailers/fig-thumbnailer.desktop
%{_datadir}/thumbnailers/odf-thumbnailer.desktop
%{_datadir}/thumbnailers/ogg-thumbnailer.desktop
%{_datadir}/thumbnailers/pdf-thumbnailer.desktop
%{_datadir}/thumbnailers/ps-thumbnailer.desktop
%{_datadir}/thumbnailers/raw-thumbnailer.desktop
%{_datadir}/thumbnailers/svgz-thumbnailer.desktop
%{_datadir}/thumbnailers/tex-thumbnailer.desktop
