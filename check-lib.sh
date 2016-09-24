#!/bin/sh
LIBNAME=wiringPi

gcc -l$LIBNAME 2>&1 | grep -q "cannot find -l$LIBNAME"
if [ $? -eq 0 ] ; then
   printf "+----------------------------------------------------------------------------------+\n"
   printf "| \033[1;31mERROR: Library wiringPi not found!\033[0m                              |\n"
   printf "| Make sure you follow instructions from http://wiringpi.com/download-and-install/ |\n"
   printf "| to install the wiringPi library on your system first then install this addon.    |\n"
   printf "+----------------------------------------------------------------------------------+\n"
   exit 0
else
   echo "Library $LIBNAME found."
fi
