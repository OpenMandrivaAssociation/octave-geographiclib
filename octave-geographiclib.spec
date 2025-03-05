%global octpkg geographiclib

Summary:	Octave/MATLAB implementation of GeographicLib
Name:		octave-geographiclib
Version:	2.3.3
Release:	1
License:	MIT
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/geographiclib/
#Source0:	https://github.com/geographiclib/geographiclib-octave/archive/v%{version}/geographiclib-octave-%{version}.tar.gz
Url:		https://github.com/geographiclib/geographiclib-octave
Source0:	https://downloads.sourceforge.net/geographiclib/distrib-Octave/geographiclib-octave-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Native Octave/MATLAB implementations of a subset of the C++ library,
GeographicLib.

Key components of this toolbox are:
 (a) Geodesics, direct, inverse, area calculations;
 (b) Projections, transverse Mercator, polar stereographic, etc;
 (c) Grid systems, UTM, UPS, MGRS;
 (d) Geoid lookup, egm84, egm96, egm2008 geoids supported;
 (e) Geometric transformations, geocentric, local cartesian;
 (f) Great ellipse, direct, inverse, area calculations. 

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-octave-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

