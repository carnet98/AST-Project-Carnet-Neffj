#!/bin/bash
cd ./tmp
gcc candidate.c -I/usr/include/csmith-2.3.0/ -g -o candidate
timeout 60s gdb -batch -x command_file.txt candidate
cd ..
