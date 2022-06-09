# Function goes here
def string_check(choice, options):

    for var_list in options:

        #if the snack is in one of the list , return full name
        if choice in var_list:

            # get full name of snack an put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        
        # if  the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is no OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

yes_no = ['yes', 'no']

check_string = "invalid choice"
while check_string == "invalid choice":
    test_question = input("Have you been given the hypotenuse? ")
    test_question = string_check(test_question, yes_no)
