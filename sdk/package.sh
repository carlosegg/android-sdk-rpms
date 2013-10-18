#!/bin/bash -x
echo "Building andorid-sdk rpms"
rpmbuild -bb SPECS/android-sdk.spec --define '_topdir '`pwd` -v --clean