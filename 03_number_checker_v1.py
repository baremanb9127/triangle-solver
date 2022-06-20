def num_check(question):

    error = "Please enter a whole number above 0. "

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here
test = num_check("What is the size of the opposite  angle? ")
test_2 = num_check("What is the size of your hypotenuse? ")
test_3 = num_check("What is the size of one side? ")
test_4 = num_check("What is the size of the adjacent angle? ")