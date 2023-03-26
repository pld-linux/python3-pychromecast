#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module		pychromecast
%define		egg_name	PyChromecast
%define		pypi_name	pychromecast
Summary:	Library for Python 3 to communicate with the Google Chromecast
Summary(pl.UTF-8):	Biblioteka Pythona 3 do komunikacji z Google Chromecast
Name:		python3-%{pypi_name}
Version:	4.1.0
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/balloob/pychromecast/archive/%{version}.tar.gz
# Source0-md5:	6f172ab76d8e7adcbbcf9a125b554cd2
URL:		https://github.com/balloob/pychromecast
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-casttube
BuildRequires:	python3-zeroconf
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for Python 3.4+ to communicate with the Google Chromecast. It
currently supports:
- Auto discovering connected Chromecasts on the network
- Start the default media receiver and play any online media
- Control playback of current playing media
- Implement Google Chromecast API v2
- Communicate with apps via channels
- Easily extendable to add support for unsupported namespaces
- Multi-room setups with Audio cast devices

%description -l pl.UTF-8
Biblioteka Pythona 3.4+ do komunikacji z Google Chromecast. Obecne
możliwości:
- automatyczne wykrywanie podłączonych Chromecastów w sieci
- uruchamianie domyślnego odbiornika i odtwarzanie treści online
- sterowanie odtwarzaniem aktualnej treści
- implementacja Google Chromecast API v2
- komunikacja z aplikacjami poprzez kanały
- łatwe rozszerzanie dodawania obsługi nowych przestrzeni nazw
- konfiguracje wielopokojowe z urządzeniami Audio cast

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{pypi_name}-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{pypi_name}-%{version}
