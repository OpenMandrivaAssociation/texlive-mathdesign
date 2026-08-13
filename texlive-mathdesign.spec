%global tl_name mathdesign
%global tl_revision 31639
%global tl_version 2.31

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Mathematical fonts to fit with particular text fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mathdesign
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdesign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdesign.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The Math Design project offers free mathematical fonts that match with
existing text fonts. To date, three free font families are available:
Adobe Utopia, URW Garamond and Bitstream Charter. Three commercial fonts
are also supported: Adobe Garamond Pro, Adobe UtopiaStd and ITC Charter.
Mathdesign covers the whole LaTeX glyph set, including AMS symbols and
some extra. Both roman and bold versions of these symbols can be used.
Moreover you can choose between three greek fonts (two of them created
by the Greek Font Society).


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from mathdesign:
Map mdbch.map
Map mdgreek.map
Map mdici.map
Map mdpgd.map
Map mdpus.map
Map mdput.map
Map mdugm.map
TL_DROPIN_EOF
