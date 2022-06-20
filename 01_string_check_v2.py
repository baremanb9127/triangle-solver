def string_check(var_list, question):

    var_list = []

    valid = False
    while not valid: 
        
        response = input(question).lower()

        for var_item in var_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
            elif response != var_item or var_item[0]:
                response == "invalid choice"
        

yes_no = ['yes', 'no']

check_string = False
while check_string == False:
    test_question = input("Have you been given the hypotenuse? ")
    test_question = string_check(yes_no)


