def string_check(question, to_check, error):

    valid = False
    while not valid: 
        
        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        
        print(error)


yes_no_list = ['yes', 'no']
favourite_thing = ['coffee', 'tea', 'water', 'juice']

rpsls = ["rock", "paper", "lizard", "scissors", "spock"]

# yes_no_list [0]
question = string_check("Are you going to the mall? ", yes_no_list, "Please enter {} or {}".format(yes_no_list[0], yes_no_list[1]))
question_two = string_check("What is your favourite beverage? ", favourite_thing, "Please enter {}, {}, {} or {}, any other opinions are irrelevant".format(favourite_thing[0], favourite_thing[1], favourite_thing[2], favourite_thing[3]))