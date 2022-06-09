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

# Main routine goes here

gk_random_q = string_check("What is your favourite thing? ", favourite_thing, "Please choose coffee, tea, water or juice")

for item in range (0,6):
    test_question = string_check("Have you been given the Hypotenuse? ", yes_no_list, "Please enter yes or no")
    print("You said {}".format(test_question))

