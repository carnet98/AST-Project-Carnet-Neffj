#!/bin/bash
cd ./tmp
gcc candidate.c -I/usr/include/csmith-2.3.0/ -g -o candidate
gdb -x command_file_name candidate
