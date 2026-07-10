%global tl_name extarrows
%global tl_revision 78315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	Extra Arrows beyond those provided in amsmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extarrows
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Arrows are provided to supplement \xleftarrow and \xrightarrow of the
amsath package: \xlongequal, \xLongleftarrow, \xLongrightarrow,
\xLongleftrightarrow, \xLeftrightarrow. \xlongleftrightarrow,
\xleftrightarrow, \xlongleftarrow and \xlongrightarrow.

