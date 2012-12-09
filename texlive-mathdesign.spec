# revision 24173
# category Package
# catalog-ctan /fonts/mathdesign
# catalog-date 2010-07-13 13:53:59 +0200
# catalog-license gpl
# catalog-version 1.55
Name:		texlive-mathdesign
Version:	1.55
Release:	2
Summary:	Mathematical fonts to fit with particular text fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mathdesign
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdesign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdesign.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The Math Design project offers free mathematical fonts, and
"faked" Caps-and-Small-Caps fonts, that fit with existing text
fonts. So far, four font families are available: - the mdput
family, which corresponds to Adobe Utopia text fonts; - the
mdugm family, which corresponds to URW Garamond text fonts; -
the mdfga family, which corresponds to the (commercial)
Fontsite Garamond text fonts; - the mdbch family, which
corresponds to Bitstream Charter text fonts. Each maths font
has a range of extra symbols, and blackboard bold and 'mathcal'
alphabets.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/mathdesign/config.mdbch
%{_texmfdistdir}/dvips/mathdesign/config.mdput
%{_texmfdistdir}/dvips/mathdesign/config.mdugm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchb8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchbc8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchbi8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchr8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchrc8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/bchri8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chb8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbi7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbi7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbi8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbi8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chbmb.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t5.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t6.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t7.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t8.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7t9.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chr8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chree.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t5.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t6.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t7.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t8.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri7t9.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chri8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chrma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdbch/md-chrmb.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utb8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbi7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbi7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbi8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbi8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utbmb.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utr8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utree.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utri7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utri7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utri8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utri8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utrma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/md-utrmb.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/putb8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/putbi8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/putr8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdput/putri8a.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmm8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmi7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmi7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmi8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmi8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmmmb.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr7v.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr7y.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr8d.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmr8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmree.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmri7m.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmri7t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmri8c.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmri8t.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmrma.afm
%{_texmfdistdir}/fonts/afm/mathdesign/mdugm/md-gmrmb.afm
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdbch.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdput.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdugm.map
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchb8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchb8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchbc8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchbc8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchbi8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchbi8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchbo8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchr8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchr8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchrc8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchrc8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchri8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchri8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/bchro8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chb8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chbo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t5.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t6.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t7.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t8.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7t9.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chree.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t5.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t6.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t7.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t8.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri7t9.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/md-chro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchb8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbic8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchboc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchbofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchric8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchroc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdbch/mdbchrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utb8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utbo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/md-utro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputb8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputbofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/mdputrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putb8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putb8x.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putb8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putbi8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putbi8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putbo8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putr8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putr8x.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putr8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putri8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putri8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdput/putro8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmm8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmo7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmmo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmree.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmro7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/md-gmro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmm8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmi7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmi7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmi8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmi8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmo7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmo8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmo8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmmofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr7v.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr7y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr8d.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmr8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmri7m.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmri7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmri8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmri8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmrma.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmrmb.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmro7t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmro8c.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmro8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/mdugmrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmm8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmm8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmmi8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmmi8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmmo8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmr8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmr8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmri8a.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmri8y.tfm
%{_texmfdistdir}/fonts/tfm/mathdesign/mdugm/ugmro8y.tfm
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb8d.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chb8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbi7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbi7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbi8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbi8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chbmb.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t5.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t6.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t7.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t8.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7t9.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr8d.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chr8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chree.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t5.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t6.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t7.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t8.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri7t9.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chri8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chrma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdbch/md-chrmb.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utb8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbi7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbi7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbi8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbi8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utbmb.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utr8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utri7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utri7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utri8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utri8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utrma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdput/md-utrmb.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmm8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmi7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmi7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmi8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmi8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmmmb.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr7v.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr7y.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmr8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmri7m.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmri7t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmri8c.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmri8t.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmrma.pfb
%{_texmfdistdir}/fonts/type1/mathdesign/mdugm/md-gmrmb.pfb
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb8d.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchb8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbi7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbi7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbi8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbi8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbic8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbo7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbo8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbo8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchboc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchbofc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr8d.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchr8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchri7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchri7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchri8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchri8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchric8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchro7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchro8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchro8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchroc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdbch/mdbchrofc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputb8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbi7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbi7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbi8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbi8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbo7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbo8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbo8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputbofc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputr8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputri7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputri7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputri8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputri8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputro7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputro8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputro8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdput/mdputrofc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm8d.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmm8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmi7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmi7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmi8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmi8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmo7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmo8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmo8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmmofc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr7v.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr7y.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr8d.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmr8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmrfc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmri7m.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmri7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmri8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmri8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmrifc8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmrma.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmrmb.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmro7t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmro8c.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmro8t.vf
%{_texmfdistdir}/fonts/vf/mathdesign/mdugm/mdugmrofc8t.vf
%{_texmfdistdir}/tex/latex/mathdesign/mathdesign.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdacmr.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdamdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbch.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbch.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdomxmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omlmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omsmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omxmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/ot1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/t1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/ts1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbcmr.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdfont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdamdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdbmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdput.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdput.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omlmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omsmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omxmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/ot1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/t1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/t1putr.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/ts1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdsffont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdttfont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdamdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdbmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdugm.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdugm.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omlmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omsmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omxmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/ot1mdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/t1mdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/ts1mdugm.fd
%_texmf_updmap_d/mathdesign
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-adobe-utopia-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-adobe-utopia-example.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-bitstream-charter-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-bitstream-charter-example.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-urw-garamond-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/MD-urw-garamond-example.pdf
%doc %{_texmfdistdir}/doc/fonts/mathdesign/README
%doc %{_texmfdistdir}/doc/fonts/mathdesign/mathdesign-doc.pdf
%doc %{_texmfdistdir}/doc/latex/mathdesign/mathdesign-doc.pdf
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdbch/MD-bitstream-charter-doc.pdf
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdbch/mdbchtest.tex
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdput/MD-adobe-utopia-doc.pdf
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdput/mdputtest.tex
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdugm/MD-urw-garamond-doc.pdf
%doc %{_texmfdistdir}/doc/latex/mathdesign/mdugm/mdugmtest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/mathdesign <<EOF
Map mdbch.map
Map mdput.map
Map mdugm.map
EOF


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.55-2
+ Revision: 753774
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.55-1
+ Revision: 718969
- texlive-mathdesign
- texlive-mathdesign
- texlive-mathdesign
- texlive-mathdesign

