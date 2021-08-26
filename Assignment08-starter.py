# -------------------------------------------------------------------------------------------------------------------- #
# Title: Assignment 08
# Description: Working with classes
# Luis Valderrama, 8.17.2021,Created started script
# Luis Valderrama, 8.21.2021,added menu options
# -------------------------------------------------------------------------------------------------------------------- #

# Objective:
# 1. The Assignment08.py script is designed to:
#       a. Present a menu of choices for the user to select from.
#       b. Execute the program based on the choice made by the user.
#       c. Use Try/Catch Error Handling.
#       d. Use Class objects.

# Improving my code:
# 1. Added Try/Except for error handling.

# Pseudo-Code:
# Data --------------------------------------------------------------------------------------------------------------- #
# Step 1 - Declare variables and constants --------------------------------------------------------------------------- #

# import sys

strChoice = ""  # Captures the user option selection
strFileName = 'products.txt'  # The name of the data file
lstOfProductObjects = []  # A list that acts as a 'table' of rows


# Processing Data----------------------------------------------------------------------------------------------------- #
# Step 2 - set up Class Product functions ---------------------------------------------------------------------------- #


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price

    changelog: (When,Who,What)
    Luis Valderrama, 8.17.2021, Created Class
    """
    # Fields --------------------------------------------------------------------------------------------------------- #
    strProductName = ""
    floatProductPrice = ""

    # Constructor ---------------------------------------------------------------------------------------------------- #
    def __init__(self, product_name, product_price):
        # -- Attributes -- #
        self.__product_name = product_name
        self.__product_price = product_price

    # Properties ----------------------------------------------------------------------------------------------------- #
    # product_name
    @property  # getter or accessor
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter  # setter or mutator
    def product_name(self, value):  # the name must match the attribute
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # product_price
    @property  # getter or accessor
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter  # setter or mutator
    def product_price(self, value):  # the name must match the attribute
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Price must be numbers")

    # Methods -------------------------------------------------------------------------------------------------------- #
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ', ' + self.product_price


# Step 3 - set up Class Processor functions--------------------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        Luis Valderrama, 8.17.2021, Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Write data to a file from a list of object rows

                :param file_name: (string) with name of file = products.txt
                :param list_of_product_objects: (list) of objects data saved to file
                :return: (bool) with status of success status
                """
        status = False
        try:
            objFile = open(file_name, 'w')
            for row in list_of_product_objects:
                objFile.write(str(row[0].strip() + ', ' + row[1]).strip() + '\n')
            objFile.close()
            status = True
        except Exception as e:
            print("File not found. The file will be created for you")
            print(e, e.__doc__, type(e), sep='\n')
        return status

    @staticmethod
    def read_data_from_file(file_name: str, list_of_product_objects: list):
        """ Reads data from a file into a list of object rows

        :param list_of_product_objects: (list) of objects data saved to file
        :param file_name: (string) with name of file = products.txt
        :return: (list) of object rows
        """

        list_of_product_objects.clear()
        try:
            objFile = open(file_name, "r")
            for row in objFile:
                lstRow = row.split(",")
                list_of_product_objects.append(lstRow)
            objFile.close()
        except Exception as e:
            print("File not found. Please select option 2, add a new product, price and select 3 to save data to file.")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_objects

# Step 4 - set up class data processor ------------------------------------------------------------------------------- #


class DataProcessor:
    """ Performs other processing data

        changelog: (When,Who,What)
        Luis Valderrama, 8.17.2021, Created Class
    """

    @staticmethod
    def add_data_to_list(list_of_product_objects: list, product_name: str, product_price: str):
        newProduct = product_name, product_price
        list_of_product_objects.append(newProduct)
        return list_of_product_objects


# End of Class ------------------------------------------------------------------------------------------------------- #

# Presentation (Input/Output) ---------------------------------------------------------------------------------------- #
# # Step 5 - set up presentation, IO functions ----------------------------------------------------------------------- #

class IO:
    """    Performs Input and Output
    changelog: (When,Who,What)
    Luis Valderrama, 8.17.2021, Created Class

    """

    @staticmethod
    def print_menu_of_Options():
        """ Display a menu of choices to the user
        :return: Nothing
        """
        print('''
            Menu of Options
            1) Display current product inventory
            2) Add a new inventory item
            3) Save data to file
            4) Exit program
            ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = int(input("Which option would you like to perform? [1 to 4] - "))
        print()
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message: An optional message to display
        :return: Nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def print_current_products_in_list(list_of_product_objects: list):
        """ Shows the current inventory

        :param list_of_product_objects: (list) split data into list
        :return: Nothing
        """

        print()
        print("******* The current inventory: *******")
        for row in list_of_product_objects:
            print(row[0] + ', ' + row[1].strip())
        print("*******************************************")
        print()

    @staticmethod
    def input_product_data():
        """
        Gets data for product object

        :return: (product) object with input data
        """
        product_name = str(input("Enter a product name: ").strip())
        product_price = str(input("Enter a price: ").strip())
        print()
        newProduct = Product(product_name, product_price)
        print("You entered: ", newProduct)
        return product_name, product_price


# End of Class ------------------------------------------------------------------------------------------------------- #

# Main Body of Script ------------------------------------------------------------------------------------------------ #
# Step 6 - Load data from file into a list of product objects when script starts ------------------------------------- #

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
except FileNotFoundError:
    IO.input_press_to_continue()

# Step 7 Use of class: ----------------------------------------------------------------------------------------------- #
while True:
    try:
        # Display menu of options ------------------------------------------------------------------------------------ #
        IO.print_menu_of_Options()
        strChoice = IO.input_menu_choice()

        # Display current inventory ---------------------------------------------------------------------------------- #
        if strChoice == 1:
            IO.print_current_products_in_list(lstOfProductObjects)
            IO.input_press_to_continue()
            continue

        # Enter new data to list ------------------------------------------------------------------------------------- #
        elif strChoice == 2:
            lstData = IO.input_product_data()
            DataProcessor.add_data_to_list(lstOfProductObjects, lstData[0], lstData[1])
            IO.print_current_products_in_list(lstOfProductObjects)
            IO.input_press_to_continue()
            continue

        # Save data from list to .txt -------------------------------------------------------------------------------- #
        elif strChoice == 3:
            print('\n Would you like to save your data?')
            strSaveToFileInput = input("Enter 'y' or 'n': ")
            if strSaveToFileInput == 'n':
                print('Data not saved!')
            if strSaveToFileInput == 'y':
                FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
                print('\nYour data is saved to', strFileName)
                IO.input_press_to_continue()
            continue

        # Ending the program and exit -------------------------------------------------------------------------------- #
        elif strChoice == 4:
            print("Goodbye!")
            EndProgram = input('\n(Press Enter to End Program)')
            break
        else:
            print('\nInvalid entry. Please enter a number from 1 to 4')
    except ValueError:
        print('\nInvalid entry. Please enter a number from 1 to 4')
