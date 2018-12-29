import json
# init block
real_number = str("+38.7")
integer_part = str("")
decimal_part = str("")
current_state = str("s_00")
event = str("unknown")
fsm_matrix = {
    "s_00":{
        "v_10":"s_10",
        "v_20":"s_10",
        "v_30":"s_10",
        "v_40":"Err_10",
        "v_50":"Err_20",
   },    
    "s_10":{
        "v_10":"Err_30",
        "v_20":"s_20",
        "v_30":"s_30",
        "v_40":"Err_40",
        "v_50":"Err_20",
   },    
    "s_20":{
        "v_10":"Err_50",
        "v_20":"s_20",
        "v_30":"s_30",
        "v_40":"END",
        "v_50":"Err_20",
   },    
    "s_30":{
        "v_10":"Err_60",
        "v_20":"s_40",
        "v_30":"Err_70",
        "v_40":"END",
        "v_50":"Err_20",
    },    
    "s_40":{
        "v_10":"Err_80",
        "v_20":"s_40",
        "v_30":"Err_90",
        "v_40":"END",
        "v_50":"Err_20",
   }    
}

# define event code
i = 0
while i < len(real_number) + 1:
    event = "s_50"
    
    if i < len(real_number):
        if real_number[i] in ["+","-"]:
            event = "v_10"

        if real_number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            event = "v_20"

        if real_number[i] in ["."]:
            event = "v_30"
    if i == len(real_number):
        event = "v_40"

    print("i:[" + str(i) +"] and event:[" + event + "]")

    # define new state
    state = fsm_matrix[current_state][event]
    previous_state = current_state
    current_state = state

    if current_state in fsm_matrix:
        if current_state == "s_20":
            integer_part += real_number[i]
        if current_state == "s_40":
            decimal_part += real_number[i]


    i += 1

print("integer_part:[" + integer_part +"] and decimal_part:[" + decimal_part + "]")



