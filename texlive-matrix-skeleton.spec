Name:		texlive-matrix-skeleton
Version:	65013
Release:	2
Summary:	A PGF/TikZ library that simplifies working with multiple matrix nodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matrix-skeleton
License:	isc
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matrix-skeleton.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matrix-skeleton.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a PGF/TikZ library that simplifies working
with multiple matrix nodes. To do so, it correctly aligns
groups of nodes with the content of the whole matrix.
Furthermore, matrix.skeleton provides rows and columns for easy
styling.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/matrix-skeleton
%doc %{_texmfdistdir}/doc/latex/matrix-skeleton

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
