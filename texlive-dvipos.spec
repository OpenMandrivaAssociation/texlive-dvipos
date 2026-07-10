%global tl_name dvipos
%global tl_revision 66186

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	support DVI pos: specials used by ConTeXt DVI output
Group:		Publishing
URL:		https://www.ctan.org/pkg/dvipos
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(dvipos.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
support DVI pos: specials used by ConTeXt DVI output

