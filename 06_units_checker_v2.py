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
    print("*** Placeholder Instructions *** ")

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


    print()
    if ab_length >= 1 and bc_length == 0 and hypotenuse_length == 0: # needs to change
        angle_check = string_check("Have you been given the size of angle BCA or BAC? (You only need one) ", (yes_no))
        # Asks user which angle they have been given
        if angle_check =='yes':
            which_angle = string_check("Which angle have you been given the size of? (BAC or BCA) ", (angle_list))
            if which_angle == 'bca':
                bca_size = num_check("What is the size of the angle BCA? ", float)
            elif which_angle == 'bac':
                bac_size = num_check("What is the size of angle BAC? ", float)
        else:
            print("Triangle is unsolvable. ")

    elif ab_length == 0 and bc_length >= 1 and hypotenuse_length == 0:
        angle_check = string_check("Have you been given the size of angle BCA or BAC? (You only need one) ", (yes_no))
        # Asks user which angle they have been given
        if angle_check =='yes':
            which_angle = string_check("Which angle have you been given the size of? (BAC or BCA) ", (angle_list))
            if which_angle == 'bca':
                bca_size = num_check("What is the size of the angle BCA? ", float)
            elif which_angle == 'bac':
                bac_size = num_check("What is the size of angle BAC? ", float)
        else:
            print("Triangle is unsolvable. ")

    elif ab_length == 0 and bc_length == 0 and hypotenuse_length >= 1:
        angle_check = string_check("Have you been given the size of angle BCA or BAC? (You only need one) ", (yes_no))
        # Asks user which angle they have been given
        if angle_check =='yes':
            which_angle = string_check("Which angle have you been given the size of? (BAC or BCA) ", (angle_list))
            if which_angle == 'bca':
                bca_size = num_check("What is the size of the angle BCA? ", float)
            elif which_angle == 'bac':
                bac_size = num_check("What is the size of angle BAC? ", float)
        else:
            print("Triangle is unsolvable. ")    

    # Solves triangle
if ab_length >= 1 and bc_length >= 1:
    # Solves triangle using pythagoras
    hypotenuse_length = math.sqrt((ab_length * ab_length) + (bc_length * bc_length))
    # need to use tan inverse
    bca_size = math.degrees(math.atan(ab_length / bc_length))
    bac_size = math.degrees(math.atan(bc_length / ab_length))
    abc_size = 90 


elif ab_length >= 1 and hypotenuse_length >= 1:
    # Solves triangle using pythagoras
    bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
    bac_size = math.degrees(math.acos(ab_length / hypotenuse_length))
    bca_size = math.degrees(math.asin(ab_length / hypotenuse_length))
    abc_size = 90

elif bc_length >= 1 and hypotenuse_length >= 1:
    # Solves triangle using pythagoras
   ac_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
   bac_size = math.degrees(math.asin(bc_length / hypotenuse_length))
   bca_size = math.degrees(math.acos(bc_length / hypotenuse_length))
   abc_size = 90

elif ab_length >= 1 and bca_size >= 1:
    # Solves triangle using trigonometry
    hypotenuse_length = ab_length / math.sin(bca_size)
    bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
    bac_size = 90 - bca_size
    abc_size = 90

elif bc_length >= 1 and bca_size >= 1:
    # Solves tri
    # angle using trigonometry
    hypotenuse_length = bc_length / math.cos(bca_size)
    ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
    bac_size = 90 - bca_size
    abc_size = 90

elif hypotenuse_length >= 1 and bca_size >= 1:
    # Solves triangle using trigonometry
    ab_length = hypotenuse_length * math.sin(bca_size)
    bc_length = hypotenuse_length * math.cos(bca_size)
    bac_size = 90 - bca_size
    abc_size = 90

elif ab_length >= 1 and bac_size >= 1:
    # Solves triangle using trigonometry
    hypotenuse_length = ab_length * math.cos(bac_size)
    bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
    bca_size = 90 - bac_size
    abc_size = 90

elif bc_length >= 1 and bac_size >= 1:
    hypotenuse_length = bc_length / math.sin(bac_size)
    ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
    bca_size = 90 - bac_size
    abc_size = 90

elif hypotenuse_length >= 1 and bac_size >= 1:
    ab_length = hypotenuse_length * math.cos(bac_size)
    bc_length = hypotenuse_length * math.sin(bac_size)
    bca_size = 90 - bac_size
    abc_size = 90

else:
    print("Triangle is unsolvable")

# Write data to file
# idk names stuff?

triangle_header = "\n *** Your SOLVED Triangle *** "

hypoenuse_print = "Hypotenuse = {} {} ".format(hypotenuse_length, units)
ab_print = "Side AB = {} {} ".format(ab_length, units)
bc_print = "Side BC = {} {} ".format(bc_length, units)
bca_print = "Angle BCA = {} ".format(bca_size)
bac_print = "Angle BAC = {} ".format(bac_size)
abc_print = "Angle ABC = 90 "

# holds list of stuff to write into file
to_write = [triangle_header, hypoenuse_print, ab_print, bc_print, bca_print, bac_print, abc_print]

# Printing Area
print("\n *** Your SOLVED Triangle *** ")

print()
print("Hypotenuse = {} {} ".format(hypotenuse_length, units))
print("Side AB = {} {} ".format(ab_length, units))
print("Side BC = {} {} ".format(bc_length, units))
print("Angle BCA = {} ".format(bca_size))
print("Angle BAC = {} ".format(bac_size))
print("Angle ABC = 90 ")

