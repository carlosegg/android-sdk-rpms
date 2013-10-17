#!/bin/bash
cd sdk
cd SOURCES
source_file=android-sdk_r22.2.1-linux.tgz
if [ ! -f $source_file ]; then
   echo "Downloading 
   curl http://dl.google.com/android/$source_filse
fi
cd ..
./build.sh
