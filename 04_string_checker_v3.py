def string_check(question, var_list):

    # generates custom error message for a list of 2 items
    if len(var_list) == 2:  
        error = "Please enter {} or {}".format(var_list[0], var_list[1]) 
    else:
        # error message includes items in the list of valid responses
        error = "Please enter "

        # includes all but the last two items
        for item in var_list[0:-2]:
            add_item = "{}, ".format(item)
            error += add_item
        
        # adds the last two items of list into error message
        error += "{} or {}".format(var_list[-2], var_list[-1])

    valid = False
    while not valid: 
        
        response = input(question).lower()
        
        # checks that respons is valid 
        for var_item in var_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
            else: 
                # Prints custom error message if response is invalid
                print(error)
                break