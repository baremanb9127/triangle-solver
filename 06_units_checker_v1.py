# Funtions go here
from re import L


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


def num_check(question, num_type):

    error = "Please enter a whole number above 0. "

    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


    
# Main Routine Goes Here 

# Set up lists / dictionaries
yes_no = ['yes', 'no']
side_list = ['hypotenuse', 'adjacent', 'opposite']
metric_list = ['cm', 'm', 'km', 'mm']
imperial_list = ['i', 'f', 'y', 'm']


# Asks user if they want to read the instructions
want_help = string_check("Do you want to read the instructions ", (yes_no))
if want_help == "yes":
    print("***PLACEHOLDER INSTRUCTIONS*** ")

# Finds out if user has been given the size of an angle
angle_check = string_check("Have you been given the size of an angle? ", (yes_no))
if angle_check == 'yes':
    angle_size = num_check("What is the size of this angle? ", float)
    if angle_size < 0 or angle_size > 89:
        print("Triangle Error - Invalid Angle ")
    else:
        print("Your first angle sizes is {} ".format(angle_size))
    second_angle_check = string_check("Have you been given the size of a second angle? ", (yes_no))
    if second_angle_check == 'yes':
        second_angle_size = num_check("What is the size of this angle? ", float)
        if angle_size + second_angle_size != 90:
            print("Triangle Error Invalid Angle ")
        else:
            print("Your second angle size is {} ".format(second_angle_size))
    

