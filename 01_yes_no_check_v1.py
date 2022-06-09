def yes_no(question):

    to_check = ['yes', 'no']

    valid = False
    while not valid: 
        
        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        
        print("Please enter yes or no... \n")

# Main routine goes here
for item in range (0,6):
    test_question = yes_no("Have you been given the Hypotenuse? ")
    print("You said {}".format(test_question))

