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

# Main routine goes here

side_list = ['hypotenuse', 'adjacent', 'opposite']
for item in range (0,6):
    get_side = string_check("What sides have you been given? ", side_list)
    print("You said {} ".format(get_side))

