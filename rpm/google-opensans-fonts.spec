%global fontname google-opensans


Name:       google-opensans-fonts
Version:    20111018
Release:    1.1
Summary:    Open Sans fonts

License:    Apache License 2.0
Url:        http://www.google.com/webfonts/specimen/Open+Sans
Group:      User Interface/X
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Open Sans is a humanist sans serif typeface designed by Steve
Matteson, Type Director of Ascender Corp. This version contains the
complete 897 character set, which includes the standard ISO Latin 1,
Latin CE, Greek and Cyrillic character sets. Open Sans was designed
with an upright stress, open forms and a neutral, yet friendly
appearance. It was optimized for print, web, and mobile interfaces,
and has excellent legibility characteristics in its letterforms.

Designer: Steve Matteson

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

%_font_pkg *.ttf

%doc

%changelog
* Sat Aug 31 2013 Andrea Bernabei <and.bernabei@gmail.com> - 1
- Initial packaging
