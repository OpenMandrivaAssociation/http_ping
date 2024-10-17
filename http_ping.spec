Summary:	HTTP latency measuring utility
Name:		http_ping
Version:	20050629
Release:	4
Group:		System/Base
License:	BSD
URL:		https://www.acme.com/software/http_ping/
Source0:	http://www.acme.com/software/http_ping/%{name}_29jun2005.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig

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

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 http_ping %{buildroot}%{_bindir}/http_ping
install -m0644 http_ping.1 %{buildroot}%{_mandir}/man1/http_ping.1

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/http_ping
%{_mandir}/man1/http_ping.1*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 20050629-3mdv2010.0
+ Revision: 429477
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 20050629-2mdv2009.0
+ Revision: 239009
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 20050629-1mdv2008.0
+ Revision: 50953
- Import http_ping



* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 20050629-1mdv2008.0
- fedora import

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050629-4
- Rebuild.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050629-3
- Convert man page to UTF-8.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050629-2
- Rebuild for new OpenSSL.

* Fri Oct 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050629-1
- Update to 29jun2005.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.0-3.20020403
- rebuilt

* Mon May  3 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20020403
- BuildRequires pkgconfig (bug 930).

* Sat Nov  1 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20020403
- First build.
