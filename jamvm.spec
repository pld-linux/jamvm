Summary:	A small Java Virtual Machine
Summary(pl):	Ma³a maszyna wirtualna Javy (JVM)
Name:		jamvm
Version:	1.3.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/jamvm/%{name}-%{version}.tar.gz
# Source0-md5:	39ec0b62717cc24d23316f8db8f026c8
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-javadir.patch
Patch2:		%{name}-i786.patch
URL:		http://jamvm.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	unzip
Requires:	classpath >= 0.12
ExclusiveArch:	arm i486 i586 i686 pentium3 pentium4 athlon ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JamVM is a new Java Virtual Machine which conforms to the JVM
specification version 2 (blue book).  In comparison to most other
VM's (free and commercial) it is extremely small, with a stripped
executable on PowerPC of only ~110K, and Intel 80K.  However, unlike
other small VMs (e.g. KVM) it is designed to support the full
specification, and includes support for object finalisation, the
Java Native Interface (JNI) and the Reflection API.

%description -l pl
JamVM jest now± maszyn± wirtualn± Javy (JVM) zgodn± z 2 wersj±
specyfikacji JVM (niebieska ksiêga). W porównaniu do wiêkszo¶ci innych
VM (darmowych i komercyjnych) jest ekstremalnie ma³a, plik wykonywalny
zajmuje na PowerPC jedynie ~110 kB, na Intelu 80 kB. Tym niemniej, w
odró¿nieniu od innych ma³ych VM (np. KVM) jest zaprojektowana, aby
obs³ugiwaæ pe³n± specyfikacjê, w³±czaj±c w to finalizacjê obiektów,
Java Native Interface i Reflection API.

%package devel
Summary:	JNI development header file
Summary(pl):	Plik nag³ówkowy dla JNI
Group:		Development/Languages/Java

%description devel
Java Native Interface development header file.

%description devel -l pl
Plik nag³ówkowy dla Java Native Interface.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
