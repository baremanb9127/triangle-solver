#Funtions go here

def string_check(question, var_list):


    valid = False
    while not valid: 
        
        response = input(question).lower()

        for var_item in var_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        
        print("error message lmao")

def number_check(question, num_type):

    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <=0:
                print("error")
            else:
                return response

        except ValueError:
            print("error")

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

# Set up lists and dictionaries
yes_no_list = ['yes', 'no']
side_list = ["Hypotenuse", "Adjacent", "Opposite"]
unit_list = ["Millimeter", "Centimeter", "Meter", "Kilometer"]\



# Asks user if they have been given thje length of the hypotenuse
get_hypotenuse = string_check("Have you been given the length of the hypotenuse? ", yes_no_list)
if get_hypotenuse == "yes":
    # Asks user for length of hypotenuse
    hypotenuse_length = number_check("What is the length of your hypotenuse? ", float)
else:
    # If user has not been given hypotenuse length - set value to zero
    hypotenuse_length = 0
    # Asks user if they have been given the length of a shorter side
    get_short_side = string_check("Have you been given the length of a shorter side? ", yes_no_list)
    if get_short_side == "yes":
        # Asks user for length of shorter side
        short_side_length = number_check("What is the length of the short side? ", float)
    else:
        # If user has not been given the first short side length - set value to zero
        short_side_length = 0
        # Proivdes error message
        if short_side_length == 0 and hypotenuse_length == 0:
            print("Triangle is unsolvable. ")
        elif short_side_length == 0 and hypotenuse_length >= 0:
            