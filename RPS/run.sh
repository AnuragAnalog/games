#!/bin/bash

gcc -c rps.c
gcc -Wall rpsmain.c rps.o -o rps
