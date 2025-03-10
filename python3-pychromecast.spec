#
# Conditional build:
%bcond_with	tests	# unit tests (not included)

%define		module		pychromecast
Summary:	Library for Python 3 to communicate with the Google Chromecast
Summary(pl.UTF-8):	Biblioteka Pythona 3 do komunikacji z Google Chromecast
Name:		python3-%{module}
# 10.3+ require protobuf >= 3.19.1
Version:	10.2.3
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/balloob/pychromecast/releases
Source0:	https://github.com/balloob/pychromecast/archive/%{version}/pychromecast-%{version}.tar.gz
# Source0-md5:	ed387a2f272ee321d98b34cc395a97a5
URL:		https://github.com/balloob/pychromecast
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-casttube >= 0.2.0
BuildRequires:	python3-protobuf >= 3.0.0
BuildRequires:	python3-zeroconf >= 0.25.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Python 3.6+ to communicate with the Google Chromecast. It
currently supports:
- Auto discovering connected Chromecasts on the network
- Start the default media receiver and play any online media
- Control playback of current playing media
- Implement Google Chromecast API v2
- Communicate with apps via channels
- Easily extendable to add support for unsupported namespaces
- Multi-room setups with Audio cast devices

%description -l pl.UTF-8
Biblioteka Pythona 3.6+ do komunikacji z Google Chromecast. Obecne
możliwości:
- automatyczne wykrywanie podłączonych Chromecastów w sieci
- uruchamianie domyślnego odbiornika i odtwarzanie treści online
- sterowanie odtwarzaniem aktualnej treści
- implementacja Google Chromecast API v2
- komunikacja z aplikacjami poprzez kanały
- łatwe rozszerzanie dodawania obsługi nowych przestrzeni nazw
- konfiguracje wielopokojowe z urządzeniami Audio cast

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pychromecast
%{py3_sitescriptdir}/PyChromecast-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
