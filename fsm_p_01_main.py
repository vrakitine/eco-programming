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
    }
}

# define event code
event = str("s_50")
i = 0
while i < len(real_number):
    event = str("unknown")

    if real_number[i] in ["+","-"]:
         event = "v_10"
        break
    if real_number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
        event = "v_20"
        break
    if real_number[i] in ["."]:
        event = "v_30"
        break

    
    i += 1

#new_state = fsm_matrix[current_state][event]


print("i:[" + str(i) +"] and event:[" + event + "]")
