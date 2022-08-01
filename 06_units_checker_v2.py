# Import Libraries
import math
import pandas

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
angle_list = ['bca', 'bac']
unit_options = ['metric', 'imperial']

# Asks user if they want to read the instructions
want_help = string_check("Do you want to read the instructions ", (yes_no))
if want_help == "yes":
    print("*** *** ")

# Get units
get_units = string_check("What measurement system are your units in? ", (unit_options))
if get_units == 'metric':
    units = string_check("What unit of measurement are you using? ", (metric_list))
elif get_units == 'imperial':
    units = string_check("What unit of measurement are you using? ", (imperial_list))

# Tells user requirements to solve a triangle
hypotenuse_check = string_check("Have you been given the length of the hypotenuse? (AC) ", (yes_no))
if hypotenuse_check == 'yes':
    hypotenuse_length = num_check("What is the length of your hypotenuse? ", float)
# Otherwise, set hypotenuse length to 0
else:
    hypotenuse_length = 0
    # Asks user if they have been given the length of the short side BC
    bc_check = string_check("Have you been given the length of the short side? (BC) ", (yes_no))
    if bc_check == "yes":
        bc_length = num_check("What is the length of the side BC? ", float)
    # Sets bc length to 0 if they haven't been provided with the length
    else: 
        bc_length = 0 
        # Asks user if they have bene given the length of the short side AB
        ab_check = string_check("Have you been given the length of the short side? (AB) ", (yes_no))
        if ab_check == "yes":
            ab_length = num_check("What is the length of the short side AB? ", float)
        else:
            # sets ab length to 0 if they can't provide a length
            ab_length = 0

if ab_length >= 1 or bc_length >= 1 or hypotenuse_length >= 1:
    angle_check = string_check("Have you been given the size of an angle? (You only need one) ", (yes_no))
    # Asks user which angle they have been given
    if angle_check =='yes':
        which_angle = string_check("Which angle have you been given the size of? ", (angle_list))
        if which_angle == 'bca':
            angle_size = num_check("What is the size of the angle BCA? ", float)
        elif which_angle == 'bac':
            angle_size = num_check("What is the size of angle BAC? ", float)
    else:
        print("Triangle is unsolvable. ")
    # Solves triangle
elif ab_length >= 1 and bc_length >= 1:
    # Solves triangle using pythagoras
    hypotenuse_length = math.sqrt((ab_length * ab_length) + (bc_length * bc_length))
    # need to use tan inverse
    angle_bca = math.tan-1(ab_length / bc_length)
    angle_bac = math.tan-1(bc_length / ab_length)
    angle_abc = 90 


elif ab_length >= 1 and hypotenuse_length >= 1:
    # Solves triangle using pythagoras
    bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
    angle_bac = math.cos-1(ab_length / hypotenuse_length)
    angle_bca = math.sin-1(ab_length / hypotenuse_length)

elif bc_length >= 1 and hypotenuse_length >= 1:
   ac_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
   angle_bac = math.sin-1(bc_length / hypotenuse_length)
   angle_bca = math.cos-1(bc_length / hypotenuse_length)
   
    # Solves triangle
else:
    print("Triangle is unsolvable")