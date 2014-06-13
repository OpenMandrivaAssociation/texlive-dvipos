# revision 29764
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-dvipos
Version:	20131012
Release:	6
Summary:	TeXLive dvipos package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dvipos.bin

%description
TeXLive dvipos package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvipos.1*
%doc %{_texmfdistdir}/doc/man/man1/dvipos.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
