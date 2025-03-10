#
# Conditional build:
%bcond_with	tests	# unit tests

%define		module	cairosvg
Summary:	Convert your SVG files to PDF and PNG
Name:		python3-%{module}
Version:	2.5.2
Release:	4
License:	LGPLv3+
Group:		Libraries/Python
Source0:	https://github.com/Kozea/CairoSVG/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	86df6285c32c1ab4a89a07fc2ad5ceea
URL:		https://cairosvg.org/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flake8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert your SVG files to PDF and PNG.

%prep
%setup -q -n CairoSVG-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/cairosvg
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/VERSION
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/CairoSVG-%{version}-py*.egg-info
