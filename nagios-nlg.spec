Summary:	Nagios Looking Glass
Name:		nagios-nlg
Version:	1.0.6
Release:	0.3
License:	Creative Commons v2.5
Group:		Applications/WWW
Source0:	http://www.andyshellam.eu/download.php?file=nlg_106.tar.gz
# Source0-md5:	9cee281a7c40c59902fc420d14e9c7db
URL:		http://www.andyshellam.eu/nlg/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/nagwatch

%description
Nagios Looking Glass is a web-based application that allows Nagios system
administrators to provide up-to-the-minute status information about their
Nagios-monitored network directly to their end users. The application is
designed to provide a read-only "dashboard" view into the network without the
complexity and security risks that arise by giving end users access to the
Nagios web console. 

%package s3_poller
Summary:	Data poller for Nagios Looking Glass
Group:		Applications/WWW
Requires:	php-common >= 4:5.0
Requires:	webserver(php)

%description s3_poller
Server-side processing of the status feeds from Nagios

%package s3_client
Summary:	Client for Nagios Looking Glass
Group:		Applications/WWW
Requires:	php-common >= 4:5.0
Requires:	webserver(php)

%description s3_client
The client that renders data from s3_poller on an AJAX-enabled web-page with
the relevant data.

%prep
%setup -q -n nlg_106
find '(' -name '*.php' -o -name '*.txt' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

rm -f client/sync-files/DELETE_ME.txt
rm -f server/index/DELETE_ME.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/s3_{client,poller}}

# s3_client
cp -a client/* $RPM_BUILD_ROOT%{_datadir}/s3_client
# s3_poller
cp -a server/* $RPM_BUILD_ROOT%{_datadir}/s3_poller

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs/*.pdf
%{_datadir}/*
