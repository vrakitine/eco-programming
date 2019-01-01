'''
Case 00
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

# V_10 => <Sign> , 
# V_20 => <digit> , 
# V_30 => <Separator> , 
# V_40 => Carriage return (CR), 
# V_50 => <Unknown> it means something different from V_10 ... V_40

fsm_matrix = {
    "s_00":{
        "comment":"initial state",
        "v_10":"s_10",
        "v_20":"s_20",
        "v_30":"s_30",
        "v_40":"Err_10",
        "v_50":"Err_20",
   },    
    "s_10":{
        "comment":"state of sign",
        "v_10":"Err_30",
        "v_20":"s_20",
        "v_30":"s_30",
        "v_40":"Err_40",
        "v_50":"Err_20",
   },    
    "s_20":{
        "comment":"state of integer part",
        "v_10":"Err_50",
        "v_20":"s_20",
        "v_30":"s_30",
        "v_40":"END",
        "v_50":"Err_20",
   },    
    "s_30":{
        "comment":"state of separator",
        "v_10":"Err_60",
        "v_20":"s_40",
       # "v_30":"Err_70" 
        "v_30":"s_30",
        "v_40":"END",
        "v_50":"Err_20",
    },    
    "s_40":{
        "comment":"state of decimal part",
        "v_10":"Err_80",
        "v_20":"s_40",
        "v_30":"Err_90",
        "v_40":"END",
        "v_50":"Err_20",
   }    
}

# input block
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



