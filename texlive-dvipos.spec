Name:		texlive-dvipos
Version:	20111101
Release:	1
Summary:	TeXLive dvipos package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-dvipos.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive dvipos package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvipos.1*
%doc %{_texmfdir}/doc/man/man1/dvipos.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
