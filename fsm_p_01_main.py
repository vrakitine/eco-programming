import json
# init block
real_number = str("+38t.7")
integer_part = str("")
decimal_part = str("")
current_state = str("s_00")
event = str("unknown")
fsm_matrix = {
    "s_00":{
        "v_10":"s_10",
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
    
    i += 1

#new_state = fsm_matrix[current_state][event]



