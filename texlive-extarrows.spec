Name:		texlive-extarrows
Version:	54400
Release:	2
Summary:	Extra Arrows beyond those provided in AMSmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extarrows
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Arrows are provided to supplement \xleftarrow and \xrightarrow
of the AMSMath package: \xlongequal, \xLongleftarrow,
\xLongrightarrow, \xLongleftrightarrow, \xLeftrightarrow.
\xlongleftrightarrow, \xleftrightarrow, \xlongleftarrow and
\xlongrightarrow.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/extarrows
%doc %{_texmfdistdir}/doc/latex/extarrows

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
