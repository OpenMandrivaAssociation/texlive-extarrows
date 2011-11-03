# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/extarrows
# catalog-date 2008-05-15 16:08:02 +0200
# catalog-license lgpl
# catalog-version 1.0b
Name:		texlive-extarrows
Version:	1.0b
Release:	1
Summary:	Extra Arrows beyond those provided in AMSmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extarrows
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Arrows are provided to supplement \xleftarrow and \xrightarrow
of the AMSMath package: \xlongequal, \xLongleftarrow,
\xLongrightarrow, \xLongleftrightarrow, \xLeftrightarrow.
\xlongleftrightarrow, \xleftrightarrow, \xlongleftarrow and
\xlongrightarrow.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/extarrows/extarrows.sty
%doc %{_texmfdistdir}/doc/latex/extarrows/README
%doc %{_texmfdistdir}/doc/latex/extarrows/extarrows-test.pdf
%doc %{_texmfdistdir}/doc/latex/extarrows/extarrows-test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
