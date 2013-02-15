Name:       alsa-lib
Summary:    The Advanced Linux Sound Architecture (ALSA) library
Version:    1.0.24.1
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.alsa-project.org/
Source0:    ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.gz


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

%description -n libasound
ALSA Library package for multimedia framework middleware package


%package -n libasound-devel
Summary:    ALSA Library package for multimedia framework middleware package
Group:      Development/Libraries
Requires:   libasound

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
%ifarch %{arm}
    --disable-alisp \
%endif
%ifarch %{arm}
    --disable-seq \
%endif
%ifarch %{arm}
    --disable-rawmidi \
%endif
%ifarch %{arm}
    --disable-python \
%endif
%ifarch %{arm}
    --with-gnu-ld \
%endif
%ifarch %{arm}
    --with-pcm-plugins=rate,linear,plug,dmix,dsnoop,asym,mmap,ioplug
%endif

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -f %{buildroot}/%{_bindir}/aserver

%post -n libasound -p /sbin/ldconfig

%postun -n libasound -p /sbin/ldconfig

%files
%manifest alsa-lib.manifest
%defattr(-,root,root,-)

%files -n libasound
%manifest alsa-lib.manifest
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/alsa-lib/smixer/*.so
%{_datadir}/alsa/*

%files -n libasound-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal

