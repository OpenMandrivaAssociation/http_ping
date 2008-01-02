Summary:	HTTP latency measuring utility
Name:		http_ping
Version:	20050629
Release:	%mkrel 1
Group:		System/Base
License:	BSD
URL:		http://www.acme.com/software/http_ping/
Source0:	http://www.acme.com/software/http_ping/%{name}_29jun2005.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
http_ping runs an HTTP fetch every few seconds, timing how long it takes.

%prep

%setup -q -n %{name}
f=http_ping.1 ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%build
%serverbuild

%make \
    CFLAGS="$CFLAGS -DUSE_SSL $(pkg-config openssl --cflags)" \
    LDFLAGS="$(pkg-config openssl --libs)"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir
install -d %{buildroot}%{_mandir}/man1

install -m0755 http_ping %{buildroot}%{_bindir}/http_ping
install -m0644 http_ping.1 %{buildroot}%{_mandir}/man1/http_ping.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/http_ping
%{_mandir}/man1/http_ping.1*
