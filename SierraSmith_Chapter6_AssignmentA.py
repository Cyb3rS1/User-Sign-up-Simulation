# Sign-up Simulation. The main purpose of this program is to compare user input with regular expression patterns
# and display whether the input is valid or not. The user's phone number, social security number, and zip code
# are tested. During this process, the user is completing their account to sign up for an unnamed service.
# At the end when their information has been verified, an account summary is shown, and they are prompted to log out.



import time
import re

DIV = "---" * 30


# main function that contains all other functions from start() to end()
def main():

    start()



# function that starts user sign-up process
def start():

    global name
    global username
    global password


    # welcome message
    print(DIV)
    print("Welcome! Ready to create a new account?")

    time.sleep(.7)

    print("\nPlease enter your information to get started.")


    # name, username, and password (won't be validated, but collected for
    # more realistic sign-up feel)
    name = input("Name: ")
    username = input("New Username: ")
    password = input("New Password: ")

    # to add some pizzazz (confidentiality), the password is converted to asterisks
    password = "*" * len(password)


    validate()



# function that prompts user for info, valid user input is stored and later used in display() function
def validate():

    # phone number, social security number, and zip code patterns
    p_pat = r"\d\d\d-\d\d\d-\d\d\d\d"

    ssn_pat = r"\d\d\d-\d\d-\d\d\d\d"

    zip_pat = r"\d\d\d\d\d"


    # dictionary that holds verification parameters. It is iterated through each time the user is prompted
    # for new information
    verif = {

        "patterns": [p_pat, ssn_pat, zip_pat],
        "info_names": ["Phone Number", "Social Security Number", "Zip Code"],
        "num_format": ["###-###-####", "###-##-####"]

    }


    # list that gets filled with only valid (verified) info, starting with phone number
    valid_info = []

    # counter for iterating through dictionary list indexes
    count = 0

    # while loop that facilitates the whole process of prompting the user for info and validating input
    while count < 3:


        # prompt for phone number and ssn; communicates required format
        if count < 2:


            print(f"Please enter your {verif["info_names"][count]} in this format: {verif["num_format"][count]}")
            user_info = input(f"{verif["info_names"][count]}: ")

        # prompt exclusively for zip code; does not communicate required format
        else:

            user_info = input(f"Please enter your {verif["info_names"][count]}: ")


        # if else statement that compares the user's input to a corresponding pattern from the verif dictionary
        if re.match(verif["patterns"][count], user_info):


            # user input gets appended to valid info
            valid_info.append(user_info)

            # if provided input is valid, add 1 to count so the next prompt will contain corresponding variables
            count += 1

        else:

            # if user input is not valid, prompt user for correct input until
            # the required format is met

            while re.match(verif["patterns"][count], user_info) is None:

                print(f"Invalid {verif["info_names"][count]}.")
                user_info = input(f"Please enter a valid {verif["info_names"][count]}: ")

            # when input is proven valid, increase counter and add into to valid_info list
            else:

                valid_info.append(user_info)

                count += 1

    # when all required info has been verified, display() is called with valid info passed in
    else:

        display(valid_info[0], valid_info[1], valid_info[2])



# function that displays all verified user input
def display(phone, ssn, zipcode):

    # account creation confirmation message
    print(f"\nAccount creation successful!")

    time.sleep(1)

    print(DIV)


    # account summary including all valid user input
    print(f"Account Summary:\n")

    print(f" Name: {name}\n Username: {username}\n Password: {password}\n"
          f" \n Phone Number: {phone}\n Social Security Number: {ssn}\n"
          f" Zip Code: {zipcode}\n")

    print(DIV)

    end()

# last function in main loop, makes the user log out. Presents a choice to create a new account
def end():

    print("This program is still under development. There's not much to do here for now.")
    input("Enter any key to logout: ")

    print(DIV)

    # log out message
    print("You have logged out. Catch you later!")

    print(DIV)

    # determining input for restarting the loop or ending it
    restart = input("Create new account? Enter y for yes or other key to exit: ")

    if restart == "y" or restart == "Y":

        # once the user has logged out, go back to start() for the next user to create a new account
        start()

    else:

        # ends program
        exit()



# call to start program
main()