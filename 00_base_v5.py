# Import Libraries
import math

# checks that the users' responses to a question are valid - creates and prints custom error message if not
def string_check(question, var_list):

    # generates custom error message for a list of 2 items
    if len(var_list) == 2:  
        error = "Please enter {} or {}".format(var_list[0], var_list[1]) 
    else:
        # error message includes items in the list of valid responses
        error = "Please enter "

        # includes all but the last two items
        for item in var_list[0:-2]:
            add_item = "{}, ".format(item)
            error += add_item
        
        # adds the last two items of list into error message
        error += "{} or {}".format(var_list[-2], var_list[-1])

    valid = False
    while not valid: 
        
        response = input(question).lower()
        
        # checks that respons is valid 
        for var_item in var_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        # Prints custom error message if response is invalid
        print(error)
        # break

# ensures that a number is entered when a number is asked for - provides helpful error message otherwise
def num_check(question, num_type, max_val = None):

    error = "Please enter a whole number above 0. "

    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            
            # Makes sure that short side is shorter than the hypotenuse length.
            if max_val is not None and response >= max_val:
                print("The hypotenuse should be the longest side. ")
                continue

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# converts a value from degrees to radians
def to_rad(degrees):
    radians = math.radians(degrees)

    return radians

# converts a value from radians to degrees
def to_deg(radians):
    degrees = math.degrees(radians)

    return degrees


# Main Routine Goes Here 




# Set up lists / dictionaries
yes_no = ['yes', 'no']
metric_list = ['cm', 'm', 'km', 'mm']
imperial_list = ['inches', 'feet', 'yards', 'miles']
angle_list = ['bca', 'bac']
unit_options = ['metric', 'imperial']

# Asks user if they want to read the instructions
want_help = string_check("Do you want to read the instructions ", (yes_no))

if want_help == "yes":
    # Prints instructions
    print("For communications sake, your triangle will be labeled as ABC, with AC being the hypotenuse. " 
        "\nTo fully solve your triangle, you need to provide either the length of any two sides or the length of one side and one angle. " 
        "\nThis program will ask you for the length of each side first - using the correct label to do so: (AB, AC and BC). "
        "\nIf you have only been given the length of one side, the program will then ask you for the size of an angle - BAC or BCA. " 
        "\nOnce the program has been provided with sufficient information, it will solve your triangle and print the values of each side and angle with the correct labels and units. ")
    print()

# Begins Loop
while True:

    # sets 'total' value to 0 - if 'total' is 1, the program asks for the value of angles.
    total = 0

    # Asks user if their units are metric or imperial
    get_units = string_check("What measurement system are your units in? (Metric or Imperial) ", (unit_options))

    # gets units
    if get_units == 'metric': 
        units = string_check("What unit of measurement are you using? ", (metric_list))
        print()
    elif get_units == 'imperial':
        units = string_check("What unit of measurement are you using? ", (imperial_list))
        print()

    # Asks user if they have the hypotenuse
    hypotenuse_check = string_check("Have you been given the length of the hypotenuse? (AC) ", (yes_no))
    if hypotenuse_check == 'yes':

        # If yes, asks user for length of hypotenuse and adds 1 to 'total' value
        hypotenuse_length = num_check("What is the length of your hypotenuse? ", float)
        print()
        total += 1

    # Otherwise, set hypotenuse length to 0
    else:
        hypotenuse_length = None

    # Asks user if they have been given the length of the short side BC
    bc_check = string_check("Have you been given the length of the short side? (BC) ", (yes_no))
    if bc_check == "yes":

        # If yes, asks user for length of the side bc and adds 1 to 'total' value
        bc_length = num_check("What is the length of the side BC? ", float, hypotenuse_length)
        print()
        total += 1

    # Otherwise, set bc length to 0
    else: 
        bc_length = 0 

    # If user has only provided the length of one side - asks user for the length of the 'third' side
    if total <= 1:
        # Asks user if they have been given the length of the short side AB
        ab_check = string_check("Have you been given the length of the short side? (AB) ", (yes_no))
        if ab_check == "yes":

            # If yes, asks user for length of the side ab and adds 1 to 'total' value
            ab_length = num_check("What is the length of the short side AB? ", float)
            print()
            total += 1

        else:
            # Otherwise, set ab length to 0
            ab_length = 0
    else:
        ab_length = 0

    print()
    # total will == 1 when the size of only one side has been provided
    if total == 1:

        # If ONLY one side has been provided, asks user if they have been given the size of an angle
        angle_check = string_check("Have you been given the size of angle BCA or BAC? (Y/N) ", (yes_no))
        
        # If yes, asks user which angle they have been given the size of
        if angle_check =='yes':
            which_angle = string_check("Which angle have you been given the size of? (BAC or BCA) ", (angle_list))
            
            # Assigns value to the correct angle
            if which_angle == 'bca':
                bca_size = num_check("What is the size of the angle BCA? ", float)
                print()
                bac_size = 0
            elif which_angle == 'bac':
                bac_size = num_check("What is the size of angle BAC? ", float)
                print()
                bca_size = 0
        else:
            print("Triangle is unsolvable. ")

    # If no values have been provided for any sides, prints 'Triangle is unsolvable.'        
    elif total == 0:
        print("Triangle is unsolvable. ")

    if hypotenuse_length == None:
        hypotenuse_length = 0

    # *** Solving Area ***
    if ab_length >= 1 and bc_length >= 1:
        # Calculates hypotenuse length using pythagoras
        hypotenuse_length = math.sqrt((ab_length * ab_length) + (bc_length * bc_length))
        # Caclulates size of angle BCA using trigonometry
        bca_size = math.degrees(math.atan(ab_length / bc_length))
        # Calculates size of angle BAC using trigonometry
        bac_size = math.degrees(math.atan(bc_length / ab_length))
        # ABC is always 90 
        abc_size = 90 


    elif ab_length >= 1 and hypotenuse_length >= 1:
        # Calculates length of side bc using pythagoras
        bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
        # Calculates size of angle BAC using trignometry
        bac_size = math.degrees(math.acos(ab_length / hypotenuse_length))
        # Calculates size of angle BCA using trigonometry
        bca_size = math.degrees(math.asin(ab_length / hypotenuse_length))
        # ABC is always 90
        abc_size = 90

    elif bc_length >= 1 and hypotenuse_length >= 1:
        # Calculates length of side AB using pythagoras
        ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
        # Calculates size of angle BAC using trigonometry
        bac_size = math.degrees(math.asin(bc_length / hypotenuse_length))
        # Calculates size of angle BCA using trigonometry
        bca_size = math.degrees(math.acos(bc_length / hypotenuse_length))
        # ABC is always 90
        abc_size = 90

    elif ab_length >= 1 and bca_size >= 1:
        bca_size = to_rad(bca_size)
        # Calcualtes hypotenuse length using trigonometry
        hypotenuse_length = ab_length / math.sin(bca_size)
        # Calculates length of BC using hypotenuse
        bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
        bca_size = to_deg(bca_size)
        # Calculates BAC size using triangle rule (all interior angles add to 180)
        bac_size = 90 - bca_size
        # ABC is always 90
        abc_size = 90

    elif bc_length >= 1 and bca_size >= 1:
        bca_size = to_rad(bca_size)
        # Calculates hypotenuse length using trigonmoetry
        hypotenuse_length = (bc_length / math.cos(bca_size))
        # Calculates AB length using pythagoras
        ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
        bca_size = to_deg(bca_size)
        # Caclulates BAC size using triangle rule
        bac_size = 90 - bca_size
        # ABC is always 90
        abc_size = 90

    elif hypotenuse_length >= 1 and bca_size >= 1:
        bca_size = to_rad(bca_size)
        # Calculates AB length using trigonometry
        ab_length = math.sin(bca_size) * hypotenuse_length
        # Caclulates BC length using trigonometry
        bc_length = math.cos(bca_size) * hypotenuse_length
        bca_size = to_deg(bca_size)
        # Calculates BAC size using triangle rule
        bac_size = 90 - bca_size
        # ABC is always 90
        abc_size = 90

    elif ab_length >= 1 and bac_size >= 1:
        bac_size = to_rad(bac_size)
        # Calculates hypotenuse length using trigonometry
        hypotenuse_length = ab_length / math.cos(bac_size)
        print("hypot", hypotenuse_length)
        print("ab length", ab_length)
        # Calculates BC length using pythagoras
        bc_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (ab_length * ab_length))
        bac_size = to_deg(bac_size)
        # Calculates BCA size using triangle rule
        bca_size = 90 - bac_size
        # ABC is always 90
        abc_size = 90

    elif bc_length >= 1 and bac_size >= 1:
        bac_size = to_rad(bac_size)
        # Calculates hypotenuse length using trigonometry
        hypotenuse_length = bc_length / math.sin(bac_size)
        # Calculates AB length using pytahgoras
        ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
        bac_size = to_deg(bac_size)
        # Calculates BCA size using triangle rule
        bca_size = 90 - bac_size
        # ABC is always 90
        abc_size = 90

    elif hypotenuse_length >= 1 and bac_size >= 1:
        bac_size = to_rad(bac_size)
        # Calculates AB length using trigonometry
        ab_length = hypotenuse_length * math.cos(bac_size)
        # Calculates BC length using trigonometry
        bc_length = hypotenuse_length * math.sin(bac_size)
        bac_size = to_deg(bac_size)
        # Calculates BCA size using triangle rule
        bca_size = 90 - bac_size
        # ABC is always 90
        abc_size = 90

    else:
        print("Triangle is unsolvable")


    # Write data to file
    triangle_header = "\n *** Your SOLVED Triangle *** "

    hypoenuse_print = "Hypotenuse = {:.2f} {} ".format(hypotenuse_length, units)
    ab_print = "Side AB = {:.2f} {} ".format(ab_length, units)
    bc_print = "Side BC = {:.2f} {} ".format(bc_length, units)
    bca_print = "Angle BCA = {} ".format(bca_size)
    bac_print = "Angle BAC = {} ".format(bac_size)
    abc_print = "Angle ABC = 90.00 "

    # holds list of stuff to write into file
    to_write = [triangle_header, hypoenuse_print, ab_print, bc_print, bca_print, bac_print, abc_print]

    # Open Text File
    file_name = "Solved_triangle.txt"
    text_file = open(file_name, "w+")

    # Write Solved Triangle to Text File
    for item in to_write:
        text_file.write(item)
        text_file.write("\n\n")

    # close file
    text_file.close()


    # Print stuff
    # Printing Area
    print("\n *** Your SOLVED Triangle *** ")

    print()
    print("Hypotenuse = {:.2f} {} ".format(hypotenuse_length, units))
    print("Side AB = {:.2f} {} ".format(ab_length, units))
    print("Side BC = {:.2f} {} ".format(bc_length, units))
    print("Angle BCA = {:.2f} ".format(bca_size))
    print("Angle BAC = {:.2f} ".format(bac_size))
    print("Angle ABC = 90.00 ")
    print()

    solve_again = string_check("Do you want to solve another triangle? ", (yes_no))
    if solve_again == "no":
        break
