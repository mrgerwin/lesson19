from cow_class import *
from sheep_class import *
import random

def auto_grow(animal, days):
    # grow the animal
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food, water)

def display_menu():
    print('1. Grow manually over 1 day')
    print('2. Grow automatically over 30 days')
    print('3. Report Status')
    print('0. Exit test program')
    print()
    print('Please select an option from the above menu')

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("option selected: "))
            if 0 <= choice <= 4:
                option_valid =True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
        elif option == 2:
            auto_grow(animal, 30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")
def manual_grow(animal):
    #get light and water values from user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10)"))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - Try again")
        except ValueError:
            print("Value entered not valid - needs to be 1 -10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value(1-10): "))
            if 1<=water<=10:
                valid = True
            else:
                print("Value entered not valid - needs to be 1-10")
        except ValueError:
            print("Value entered not valid - needs to be 1-10")
    animal.grow(food, water)

def top_menu():
    print()
    print("which animal would you like to create?")
    print()
    print("1. Sheep")
    print("2. Cow")
    print()
    print("Please select an option")
    
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Options selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def create_animal():
    top_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep()
    elif choice == 2:
        new_animal = Cow()
    return new_animal

def main():
    new_animal = create_animal()
    manage_animal(new_animal)

if __name__== "__main__":
    main()