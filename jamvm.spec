Summary:	A small Java Virtual Machine
Summary(pl):	Ma�a maszyna wirtualna Javy (JVM)
Name:		jamvm
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7f5c459d6b900e0c8248900ab007289e
Patch0:		%{name}-libdir.patch
URL:		http://jamvm.sourceforge.net/
Requires:	classpath >= 0.09
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
JamVM jest now� maszyn� wirtualn� Javy (JVM) zgodn� z 2 wersj�
specyfikacji JVM (niebieska ksi�ga). W por�wnaniu do wi�kszo�ci innych
VM (darmowych i komercyjnych) jest ekstremalnie ma�a, plik wykonywalny
zajmuje na PowerPC jedynie ~110 kB, na Intelu 80 kB. Tym niemniej, w
odr�nieniu od innych ma�ych VM (np. KVM) jest zaprojektowana, aby
obs�ugiwa� pe�n� specyfikacj�, w��czaj�c w to finalizacj� obiekt�w,
Java Native Interface i Reflection API.

%package devel
Summary:	JNI development header file
Summary(pl):	Plik nag��wkowy dla JNI
Group:		Development/Languages/Java

%description devel
Java Native Interface development header file.

%description devel -l pl
Plik nag��wkowy dla Java Native Interface.

%prep
%setup -q
%patch0 -p0

%build
%configure \
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
