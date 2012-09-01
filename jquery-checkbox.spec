# TODO
# - paths and deps for demo
%define		plugin	checkbox
Summary:	jQuery custom CSS styled checkboxes (and radio buttons, too)
Name:		jquery-%{plugin}
Version:	1.3.0
Release:	0.beta1.1
License:	MIT
Group:		Applications/WWW
Source0:	https://jquery-checkbox.googlecode.com/files/jquery-checkbox.%{version}b1.zip
# Source0-md5:	3b4c993af810fa82b8e0a1a206ce0952
URL:		https://code.google.com/p/jquery-checkbox/
BuildRequires:	closure-compiler
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A replacement for the standard checkbox that allows you to change the
look of checkbox elements in your page.

Features:
- only inline elements used, just like default checkoxes
- cross-browser look and feel (tested in IE6, IE7, IE8, Firefox and
  Chrome engines)
- work with radio buttons too
- supports inline and jQuery attached click events
- supports "label hovering": when you point over parent label element,
  it will highlight its checkbox (thanks to Eugene for the idea)
- dynamic skin changing
- adds new checkbox events "check", "uncheck", "disable", "enable",
  ready to use in jQuery.bind() method

%package demo
Summary:	Demo for jQuery.checkbox
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.checkbox
Group:		Development
URL:		http://widowmaker.kiev.ua/checkbox/
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.checkbox.

%prep
%setup -qc

%build
install -d build

# pack .css
for css in *.css; do
	out=build/${css#*/jquery.}
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $css -o $out
%else
	cp -p $css $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p build/jquery.%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p jquery.%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css
cp -p build/jquery.safari-%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/safari-%{plugin}-%{version}.min.css
cp -p jquery.safari-%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/safari-%{plugin}-%{version}.css
ln -s safari-%{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/safari-%{plugin}.css

cp -p checkbox.png empty.png safari-checkbox.png $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p index.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p screenshot.png $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
