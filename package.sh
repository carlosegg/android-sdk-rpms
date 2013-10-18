#!/bin/bash
cd sdk
mkdir -p SOURCES
cd SOURCES
source_file=android-sdk_r22.2.1-linux.tgz
if [ ! -f $source_file ]; then
   echo "Downloading $source_file"
   wget http://dl.google.com/android/$source_file
fi
cd ..
$0
