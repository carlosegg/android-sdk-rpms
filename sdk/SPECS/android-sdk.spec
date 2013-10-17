Name:       android-sdk
Version:    22.2.1
Release:    1
Summary:    android-sdk
Group:      develenv
License:    http://creativecommons.org/licenses/by/2.5/
Packager:   softwaresano.com
URL:        http://developer.android.com/sdk/index.html
Source0:    %{package_name}_r%{version}-linux.tgz
BuildArch:  x86_64
BuildRoot:  %{_topdir}/BUILDROOT
Requires:   jdk > 1.7
Vendor:     softwaresano.com

%define __jar_repack 0
%define package_name android-sdk
%define project_parent_name develenv
%define target_dir  /opt/ss/%{project_parent_name}/platform/

%description
The Android SDK provides you the API libraries and developer tools necessary to 
build, test, and debug apps for Android.

%install
%{__mkdir_p} %{buildroot}/%{target_dir}
cd  %{buildroot}/%{target_dir}
tar xvfz %{SOURCE0}

%clean
[ %{buildroot} != "/" ] && rm -rf %{buildroot}

%pre
#Create develenv user if not exists
# Creating develenv user if the installations is out of develenv
 id -u %{project_parent_name} || useradd -s /bin/bash %{project_parent_name}

%post

%files
%defattr(-,%{project_parent_name},%{project_parent_name},-)
%{target_dir}


%changelog
