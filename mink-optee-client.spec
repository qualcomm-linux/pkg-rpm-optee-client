Name:		mink-optee-client
Version:	4.0.0
Release:	1%{?dist}
Summary:	Qualcomm mink based optee client library for PKCS#11

License:	BSD-2-Clause
URL:		https://github.com/OP-TEE/optee_client
Source0:	https://github.com/OP-TEE/optee_client/archive/refs/tags/%{version}.tar.gz#/optee_client-%{version}.tar.gz
Patch0:		add-teec-trace-file.patch
Patch1:		build-libckqteec.patch

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	minkipc-devel

%description
This package provides libckqteec, a Qualcomm-adapted build of the upstream
OP-TEE PKCS11 TEE client library. It is built against the Qualcomm MinkIPC
transport layer (libminkteec, libminkadaptor) and is designed to communicate
with the Qualcomm Trusted Execution Environment (QTEE).

This package contains the libckqteec shared library.


%package devel
Summary: Development files for the libckqteec library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files needed to build and link to the libckqteec library.


%prep
%setup -q -n optee_client-%{version}
%patch -P0 -P1 -p1


%build
echo "build host: $(hostname) uid=$(id -u) vars: $(printenv | cut -d= -f1 | sort | paste -sd, -)"
%cmake
%cmake_build


%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libckqteec.so.*

%files devel
%{_libdir}/libckqteec.so
%{_includedir}/ck_debug.h
%{_includedir}/pkcs11.h
%{_includedir}/pkcs11_ta.h


%changelog
* Wed Sep 02 2026 Abhinaba Rakshit <abhinaba.rakshit@oss.qualcomm.com> - 4.0.0-1
- Initial RPM package with upstream v4.0.0
