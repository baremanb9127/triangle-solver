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

yes_no_list = ['yes', 'no']
favourite_thing = ['coffee', 'tea', 'water', 'juice']

rpsls = ["rock", "paper", "scissors", "lizard", "spock"]

list_errors(yes_no_list)
print()
list_errors(favourite_thing)
print()
list_errors(rpsls)