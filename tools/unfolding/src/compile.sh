#!/bin/bash
current_PATH='./*.cpp'
dcr2cpn_PATH='./dcr2cpn/*.cpp'
ltl2prop_PATH='./ltl2prop/*.cpp'

g++ -c ./ltl2prop/*.cpp  -c ./dcr2cpn/*.cpp -c ./*.cpp

