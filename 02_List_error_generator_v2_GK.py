

yes_no_list = ['yes', 'no']
favourite_thing = ['coffee', 'tea', 'water', 'juice']

rpsls = ["rock", "paper", "lizard", "scissors", "spock"]

error = "Please enter "
for item in rpsls[0:2]:
    add_item = "{}, ".format(item)
    error += add_item

error += "and {}".format(rpsls[3])


print(error)

print(rpsls[-2])
print(rpsls[-1])
