#!/bin/bash
current_PATH='./*.cpp'
dcr2cpn_PATH='./dcr2cpn/*.cpp'
ltl2prop_PATH='./ltl2prop/*.cpp'

g++ -c "$dcr2cpn_PATH"  -c "$ltl2prop_PATH" -c "$current_PATH"


# #!/bin/bash
# src_PATH='./src/*.o'
# include_PATH='../include/*.o'
# input_FILE='unfolding.cpp'
# output_FILE="unfolding"

# # g++ "$input_FILE" "$src_PATH" "$include_PATH" -o "$output_FILE"

# #g++ -c "$dcr2cpn_PATH"  -c "$ltl2prop_PATH" -c "$current_PATH"
# g++ -c ./dcr2cpn/*.cpp  -c ./ltl2prop/*.cpp -c ./*.cpp
