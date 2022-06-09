

yes_no_list = ['yes', 'no']
favourite_thing = ['coffee', 'tea', 'water', 'juice']

rpsls = ["rock", "paper", "scissors", "lizard", "spock"]
    


if  len(rpsls) == 2:
    error = "Please enter "
    for item in yes_no_list[0:1]:
        add_item = "{} ".format(item)
        error += add_item

    error += "or {}".format(yes_no_list[-1]) 
else:
    error = "Please enter "
    for item in rpsls[0:3]:
        add_item = "{}, ".format(item)
        error += add_item

    error += "{} or {}".format(rpsls[-2], rpsls[-1])

print(error)