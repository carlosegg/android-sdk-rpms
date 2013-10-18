#!/bin/bash -x
echo "Building maven-repos"
rpmbuild -bb SPECS/mavenrepos.spec --define '_topdir '`pwd` -v --clean