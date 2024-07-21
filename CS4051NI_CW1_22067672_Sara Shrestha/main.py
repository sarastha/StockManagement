# Importing all the python files
import read
import sale
import purchase
import overwrite
from datetime import datetime

# Defining a main option to compile all the functions and call them accordingly
def main_option():
    # display of main menu interface after the program is executed
    print("\n")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t \tSara Electronics")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t \t \t \t \tNaya Bazaar, Kathmandu | Phone No: 9823099951")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t Welcome to the Sara's Electronics")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    # provide details to perform a specific action the customer wants
    loop = True
    while loop == True:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tChoose any one option to continue shopping in our store:")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("\t\t\t\t\t\t                 OPTIONS               \n")
        print("\t\t\t\t           Press [1] to View the list of laptops to the customer.   \n")
        print("\t\t\t\t           Press [2] to Sale the laptop to the customer.   \n")
        print("\t\t\t\t           Press [3] to Purchase laptops from manufacturer.    \n")
        print("\t\t\t\t           Press [4] to Exit from the system.          \n")
        print("\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        # ask for the customer to input the action to be performed
        user_input = int(input("Enter the option you would like to continue: "))
        print("\n")

        #calling the function of laptop list reading when the customer wants to view all the available laptops
        if user_input == 1:
            a = read.read_laptop()
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

        #calling the function of laptop selling when customer wants to buy any laptop
        elif user_input == 2:
            #calling function to display all the available laptops
            a = read.read_laptop()
            # Passing of the returned list from the laptop read file on the laptop sale function
            b = sale.sale_laptops(a)
            # Passing of the returned list and dictionary from the laptop read file and sale laptop function respectively to overwrite the txt file
            overwrite.over_writing_sale(a, b)
            print()
            # Ask the user to if they'd wish to progress with another transaction or not
            ask_again = input("Do you wish to proceed for more transactions (Y/N)? ").upper()
            print()
            print("-----------------------------------------------------------------------------------------------------------------------")
            if ask_again == "N":
                break
        
        elif user_input == 3:
            #calling function to display all the available laptops
            a = read.read_laptop()
            # Passing of the returned list from the laptop read file on the laptop sale function
            b = purchase.laptop_purchase(a)
            # Passing of the returned list and dictionary from the laptop read file and sale laptop function respectively to overwrite the txt file
            overwrite.over_writing_purchase(a, b)
            print()
            # Ask the user to if they'd wish to proceed with another transaction or not
            ask_again = input("Do you wish to proceed for more transactions (Y/N)? ").upper()
            print()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            if ask_again == "N":
                break
            print("Thank you for purchasing the laptop. ")
            print("\n")
        elif user_input == 4:
            loop = False
            print("Happy Shopping! ")
            print("\n")
        else:
            print("Your option", user_input,"does not seem to match as per our requirement. Please look at the provided option.")
            print("\n")
            

# calling of main option function to perform all the actions
main_option()
print()
print("Thank you for visiting our store.")
print()
print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        
    




    

    



    

    
    

    
