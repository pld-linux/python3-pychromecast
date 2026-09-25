%define		module		pychromecast
Summary:	Library for Python 3 to communicate with the Google Chromecast
Summary(pl.UTF-8):	Biblioteka Pythona 3 do komunikacji z Google Chromecast
Name:		python3-%{module}
Version:	14.0.10
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/home-assistant-libs/pychromecast/releases
Source0:	https://github.com/home-assistant-libs/pychromecast/archive/%{version}/pychromecast-%{version}.tar.gz
# Source0-md5:	7555f36e4f578cbd065b3b2e1914216b
Patch0:		%{name}-build-caps.patch
URL:		https://github.com/home-assistant-libs/pychromecast
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools >= 1:65.6
BuildRequires:	python3-wheel >= 0.37.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Python 3.11+ to communicate with the Google Chromecast. It
currently supports:
- Auto discovering connected Chromecasts on the network
- Start the default media receiver and play any online media
- Control playback of current playing media
- Implement Google Chromecast API v2
- Communicate with apps via channels
- Easily extendable to add support for unsupported namespaces
- Multi-room setups with Audio cast devices

%description -l pl.UTF-8
Biblioteka Pythona 3.11+ do komunikacji z Google Chromecast. Obecne
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
%patch -P0 -p1

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pychromecast
%{py3_sitescriptdir}/pychromecast-%{version}.dist-info
%{_examplesdir}/python3-%{module}-%{version}
