%global packname  mondate
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.9.9.01
Release:          1
Summary:          Keep track of dates in terms of months
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-utils R-methods 
Requires:         R-zoo 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils R-methods
BuildRequires:    R-zoo 

%description
Keep track of dates in month units.  Perform date arithmetic in "months"
(default), "years", and "days".  Enable dates to have "shape" (non NULL
dim).  Allow "infinite" dates.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
