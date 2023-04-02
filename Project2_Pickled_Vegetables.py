##################################################################################################################################################
# Program: m7 homework #7 Dictionaries/Sets/Serialization: 2. Pickled Vegetables
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 4/1/23
##################################################################################################################################################

# Write a program that keeps vegetable names and prices in a dictionary as key-value pairs.
#
# The program should display a menu that lets the user: 
#   see a list of all vegetables and their prices,
#   add a new vegetable and price, 
#   change the price of an existing vegetable, 
#   and delete an existing vegetable and price.
#
# The program should pickle the dictionary and save it to a
# file called vegetables.dat when the user exits the program. Each time the program starts,
# it should retrieve the dictionary from the file and unpickle it.

import pickle

def main():
    try:
        # Unpickle menu from file and setting
        menu = UnPickleMenu()
    except:
        # Creating a menu of vegetables
        menu = create_menu()

        # Pickle the menu
        PickleMenu(menu)

    # Function Calls:

    # See menu items and its prices
    SeeMenu(menu)

    print()
    menu = AddVegie(menu)    # Add a new vegie with price to menu
    print()
    SeeMenu(menu) # Look at menu

    print()
    menu = ChangePrice(menu) # Change the price of an existing vegie
    print()
    SeeMenu(menu) # Look at menu

    print()
    DeleteMenuItem(menu)    # Delete an existing vegie and price from menu
    print()
    SeeMenu(menu) # Look at menu


def create_menu():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    menu = {'Carrot': 2.00, 'Red Onion': 2.50, 'Green Onion': 3.00,
            'Radish': 3.25, 'Bell Pepper': 3.50, 'Artichoke': 5.00}
    
    # Return the deck.
    return (menu)
    
def SeeMenu(menu):
    """ Allows User to see Menu."""
    print('Here is the menu for vegetables and their prices:\n')
    for vegie,price in menu.items():
        print(vegie + f': ${price: ,.2f}')

def AddVegie(menu):
    """ User Adds a new Vegetable to menu. """
    new_vegie = input("Enter a vegie to add to menu: ")
    price = input("Enter the price for new vegie: $")

    # Adding to menu
    menu.update({str(new_vegie): float(price)})

    # Returning updated Menu to main
    return (menu)

def ChangePrice(menu):
    """ Change the price of an existing vegie. """
    # Initializing variable for new price
    new_price = 0
    existing_vegie = input('Enter an existing vegie: ')

    if existing_vegie in menu:
        print('Vegie found!')
        new_price = input('Enter the new price of vegie: ')
        menu[existing_vegie] = float(new_price) # Existing vegie has new price
    else:
        print('Vegie has not been found.')
        print('Try again.\n')
        ChangePrice(menu) # Function reccurrsion 

    # Returning changed Menu to main
    return (menu)

def DeleteMenuItem(menu):
    """ Delete an existing vegie and price. """
    existing_vegie = input('Enter an existing vegie to delete from menu: ')

    if existing_vegie in menu:
        print('Vegie found!')
        del menu[existing_vegie]
        print('Vegie and price have been deleted from menu.')
    else:
        print('Vegie has not been found.')
        print('Try again.\n')
        DeleteMenuItem(menu) # Function reccurrsion 

    # Returning Menu with deleted vegie to main
    return (menu)

def PickleMenu(menu):
    """ Pickle the dictionary. """
    filename = 'vegetables.dat'
    outfile = open(filename, 'wb')  # Outputting file in binary
    pickle.dump(menu,outfile)
    outfile.close()

def UnPickleMenu():
    readfile = open('vegetables.dat','rb')  # Reading binary file

    # Setting menu
    file_menu = pickle.load(readfile)

    readfile.close()
    return file_menu

# Call the main function
if __name__ == '__main__':
    main()