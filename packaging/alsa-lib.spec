#sbs-git:slp/pkgs/a/alsa-lib alsa-lib 1.0.21a cb38cd61f9258cb9c7ea768f9782b372de5976df
Name:       alsa-lib
Summary:    The Advanced Linux Sound Architecture (ALSA) library
Version:    1.0.24.1
Release:    6
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.alsa-project.org/
Source0:    ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.gz
Obsoletes:  alsa-lib-1.0.25
Conflicts:  alsa-lib-1.0.25


%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.


%package -n libasound
Summary:    ALSA Library package for multimedia framework middleware package
Group:      Development/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Obsoletes:  libasound-1.0.25
Conflicts:  libasound-1.0.25

%description -n libasound
ALSA Library package for multimedia framework middleware package


%package -n libasound-devel
Summary:    ALSA Library package for multimedia framework middleware package
Group:      Development/Libraries
Requires:   libasound
Obsoletes:  libasound-1.0.25-devel
Conflicts:  libasound-1.0.25-devel

%description -n libasound-devel
ALSA Library package for multimedia framework middleware package


%prep
%setup -q


%build
export CFLAGS+=" -fPIC" 
export LDFLAGS+=" -Wl,--warn-unresolved-symbols -Wl,--hash-style=both -Wl,--as-needed"
chmod +x autogen.sh

%autogen --disable-static
%configure --disable-static \
%ifarch %{arm}
    --with-alsa-devdir=/dev/snd \
%endif
    --disable-alisp \
    --disable-seq \
    --disable-rawmidi \
    --disable-python \
    --with-gnu-ld \
%ifarch %{arm}
    --with-pcm-plugins=rate,linear,plug,dmix,dsnoop,asym,mmap,ioplug
%endif

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}
cp COPYING %{buildroot}/usr/share/license/libasound
%make_install

rm -f %{buildroot}/%{_bindir}/aserver

%post -n libasound -p /sbin/ldconfig

%postun -n libasound -p /sbin/ldconfig

%files
%manifest alsa-lib.manifest
%defattr(-,root,root,-)
%{_datadir}/license/%{name}

%files -n libasound
%manifest alsa-lib.manifest
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/alsa-lib/smixer/*.so
%{_datadir}/alsa/*
%{_datadir}/license/libasound

%files -n libasound-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal
