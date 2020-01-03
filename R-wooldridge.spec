#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-wooldridge
Version  : 1.3.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/wooldridge_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/wooldridge_1.3.1.tar.gz
Summary  : 111 Data Sets from "Introductory Econometrics: A Modern
Group    : Development/Tools
License  : GPL-3.0
Requires: R-formatR
Requires: R-prais
Requires: R-stargazer
BuildRequires : R-formatR
BuildRequires : R-prais
BuildRequires : R-stargazer
BuildRequires : buildreq-R

%description
[![CRAN_Status_Badge](https://www.r-pkg.org/badges/version/wooldridge)](https://cran.r-project.org/package=wooldridge) [![Travis](https://travis-ci.org/JustinMShea/wooldridge.svg?branch=master)](https://travis-ci.org/JustinMShea/wooldridge) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/JustinMShea/wooldridge?branch=master&svg=true)](https://ci.appveyor.com/project/JustinMShea/wooldridge)   [![](https://cranlogs.r-pkg.org/badges/wooldridge)](https://CRAN.R-project.org/package=wooldridge)

%prep
%setup -q -c -n wooldridge

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573483488

%install
export SOURCE_DATE_EPOCH=1573483488
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wooldridge
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wooldridge
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library wooldridge
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc wooldridge || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/wooldridge/DESCRIPTION
/usr/lib64/R/library/wooldridge/INDEX
/usr/lib64/R/library/wooldridge/Meta/Rd.rds
/usr/lib64/R/library/wooldridge/Meta/data.rds
/usr/lib64/R/library/wooldridge/Meta/features.rds
/usr/lib64/R/library/wooldridge/Meta/hsearch.rds
/usr/lib64/R/library/wooldridge/Meta/links.rds
/usr/lib64/R/library/wooldridge/Meta/nsInfo.rds
/usr/lib64/R/library/wooldridge/Meta/package.rds
/usr/lib64/R/library/wooldridge/Meta/vignette.rds
/usr/lib64/R/library/wooldridge/NAMESPACE
/usr/lib64/R/library/wooldridge/NEWS.md
/usr/lib64/R/library/wooldridge/R/wooldridge
/usr/lib64/R/library/wooldridge/R/wooldridge.rdb
/usr/lib64/R/library/wooldridge/R/wooldridge.rdx
/usr/lib64/R/library/wooldridge/data/Rdata.rdb
/usr/lib64/R/library/wooldridge/data/Rdata.rds
/usr/lib64/R/library/wooldridge/data/Rdata.rdx
/usr/lib64/R/library/wooldridge/data/datalist
/usr/lib64/R/library/wooldridge/doc/Introductory-Econometrics-Examples.R
/usr/lib64/R/library/wooldridge/doc/Introductory-Econometrics-Examples.Rmd
/usr/lib64/R/library/wooldridge/doc/Introductory-Econometrics-Examples.html
/usr/lib64/R/library/wooldridge/doc/index.html
/usr/lib64/R/library/wooldridge/help/AnIndex
/usr/lib64/R/library/wooldridge/help/aliases.rds
/usr/lib64/R/library/wooldridge/help/paths.rds
/usr/lib64/R/library/wooldridge/help/wooldridge.rdb
/usr/lib64/R/library/wooldridge/help/wooldridge.rdx
/usr/lib64/R/library/wooldridge/html/00Index.html
/usr/lib64/R/library/wooldridge/html/R.css
/usr/lib64/R/library/wooldridge/tests/testthat.R
/usr/lib64/R/library/wooldridge/tests/testthat/test_data.R
