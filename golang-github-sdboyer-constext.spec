# https://github.com/sdboyer/constext
%global goipath         github.com/sdboyer/constext
%global commit          836a144573533ea4da4e6929c235fd348aed1c80

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Cons Contexts together as a pair
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}



%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch


%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git836a144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1
- First package for Fedora
  resolves: #1556894
