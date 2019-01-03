'''
You can use python emulator online 
https://www.onlinegdb.com/online_python_interpreter
for the code below. Just simple copy and paste code to the emulator.
Enjoy!

'''

import json
# init block
real_number = str("-56.78")
integer_part = str("")
decimal_part = str("")
current_state = str("s_00")
previous_state = str("s_00")
event = str("unknown")

# input block
path = "p_01_040_plus/"
case_number = input("\nInput case_number? ")
fsm_matrix_file_name = case_number + "_case_fsm_matrix.json"
full_name = path + fsm_matrix_file_name
with open(full_name, 'r') as f:
    fsm_matrix = json.load(f)

print("Loaded data from:[" + full_name + "]")

real_number = input("\nInput real_number? ")

# define event code
i = 0
while i < len(real_number) + 1:
    event = "v_50"
    
    if i < len(real_number):
        if real_number[i] in ["+","-"]:
            event = "v_10"

        if real_number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            event = "v_20"

        if real_number[i] in ["."]:
            event = "v_30"
    if i == len(real_number):
        event = "v_40"


    # define new state
    state = fsm_matrix[current_state][event]
    previous_state = current_state
    current_state = state
    
    if i < len(real_number):
        print("\ni:[" + str(i) +"] | event:[" + event + "] | real_number[i]:[" + real_number[i] + "] | previous_state:[" + previous_state + "] | current_state:[" + current_state + "] ")


    if current_state in fsm_matrix:
        if current_state == "s_20":
            integer_part += real_number[i]
        if current_state == "s_40":
            decimal_part += real_number[i]
        i += 1
        continue
    break

if current_state.find("END") != 0:
       print("\n\n\nError code:[" + current_state +"]\n\n")

if current_state.find("END") == 0: 
    print("\n\ninteger_part:[" + integer_part +"] and decimal_part:[" + decimal_part + "]\n")



