def string_check(question, to_check): 

    valid = False
    while not valid: 
        
        response = input(question).lower()

        if response in to_check:
            return response
        
        else:
            for item in to_check:
                if response == item [0]:
                    return item




def list_errors(var_list):

    if  len(var_list) == 2:
        error = "Please enter {} or {}".format(var_list[0], var_list[1]) 
    else:
        error = "Please enter "
        for item in var_list[0:-2]:
            add_item = "{}, ".format(item)
            error += add_item

        error += "{} or {}".format(var_list[-2], var_list[-1])

    print(error)

# Main routine goes here

side_list = ["Hypotenuse", "Adjacent", "Opposite"]

get_side = string_check("What side have you been provided with? ", [side_list])
print("You have the", get_side)