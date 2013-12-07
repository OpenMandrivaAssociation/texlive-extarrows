# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/extarrows
# catalog-date 2008-05-15 16:08:02 +0200
# catalog-license lgpl
# catalog-version 1.0b
Name:		texlive-extarrows
Version:	1.0b
Release:	4
Summary:	Extra Arrows beyond those provided in AMSmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extarrows
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extarrows.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/extarrows/extarrows.sty
%doc %{_texmfdistdir}/doc/latex/extarrows/README
%doc %{_texmfdistdir}/doc/latex/extarrows/extarrows-test.pdf
%doc %{_texmfdistdir}/doc/latex/extarrows/extarrows-test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-2
+ Revision: 751728
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-1
+ Revision: 718403
- texlive-extarrows
- texlive-extarrows
- texlive-extarrows
- texlive-extarrows

