Summary:	A small Java Virtual Machine
Summary(pl.UTF-8):	Mała maszyna wirtualna Javy (JVM)
Name:		jamvm
Version:	1.5.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/jamvm/%{name}-%{version}.tar.gz
# Source0-md5:	5a82751b50391eb092c906ce64f3b6bf
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-i786.patch
URL:		http://jamvm.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%ifarch %{x8664} hppa
BuildRequires:	libffi-devel
%endif
BuildRequires:	libtool
BuildRequires:	unzip
BuildRequires:	zlib-devel
Requires:	classpath >= 0.19
ExclusiveArch:	%{ix86} %{x8664} arm hppa mipsel ppc
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JamVM is a new Java Virtual Machine which conforms to the JVM
specification version 2 (blue book).  In comparison to most other
VM's (free and commercial) it is extremely small, with a stripped
executable on PowerPC of only ~110K, and Intel 80K.  However, unlike
other small VMs (e.g. KVM) it is designed to support the full
specification, and includes support for object finalisation, the
Java Native Interface (JNI) and the Reflection API.

%description -l pl.UTF-8
JamVM jest nową maszyną wirtualną Javy (JVM) zgodną z 2 wersją
specyfikacji JVM (niebieska księga). W porównaniu do większości innych
VM (darmowych i komercyjnych) jest ekstremalnie mała, plik wykonywalny
zajmuje na PowerPC jedynie ~110 kB, na Intelu 80 kB. Tym niemniej, w
odróżnieniu od innych małych VM (np. KVM) jest zaprojektowana, aby
obsługiwać pełną specyfikację, włączając w to finalizację obiektów,
Java Native Interface i Reflection API.

%package devel
Summary:	JNI development header file
Summary(pl.UTF-8):	Plik nagłówkowy dla JNI
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description devel
Java Native Interface development header file.

%description devel -l pl.UTF-8
Plik nagłówkowy dla Java Native Interface.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure \
	%{?debug:--enable-trace} \
	--with-classpath_install_dir=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D src/jni.h $RPM_BUILD_ROOT%{_includedir}/jni.h

# unwanted symlink
rm $RPM_BUILD_ROOT%{_libdir}/rt.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/jamvm
%attr(755,root,root) %{_libdir}/libjvm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjvm.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjvm.so
%{_libdir}/libjvm.la
%{_includedir}/jni.h
