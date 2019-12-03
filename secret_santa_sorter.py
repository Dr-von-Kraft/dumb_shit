'''

Codename: Secret Santa Sorter

Author: Dr_Von_Kraft, also know as SC

Purpose of code:

After spending many a year with my family doing secret santa gifts, we would always moan
when someone got their own name and had to do it all over again.

With this code, it reshuffles the collected names until it had them all sorted out.
This means that the code will always produce a batch of .txt files that have been
sorted with out the a person getting their own name back.

Date last modified: 02/12/2019

'''

# Random is inported so the code can randomize numbers
import random

#-------------------------------------------FUNCTIONS--------------------------------------

def welcome_message():
    ''' A welcome message that gets displayed on the screen when someone activates main() AKA starts the program'''
    
    print('\n***************************************************************************************')
    print("\nWelcome to the secret santa sorter program!")
    print("\nThis program has very simple rules for running it:")
    print("\n1. The program will ask for names. Simply type them in and hit enter!")
    print("\n2. After entering in the last name, type \"exit\" and the name will be stored")
    print("\n3. Confirm that the names displayed are correct")
    print("\n4. Once confirmed, the program will mix up the names, and store them in .txt files.")
    print("   These files will have an idividual's name on it, and inside will be the name of person")
    print("   they will get a present for.")
    print("\n\n   And last but not least, the program ensures no one gets their own name back. Enjoy!")

def name_collector():
    ''' This collects names from the user and returns it to main()'''
    
    names = []
    userInput = ''
    # Checks that the user is still inputing names
    while userInput != 'exit':
        userInput = input("\nPlease enter a name for the sorter: ")
        names.append(userInput)
    return names


def the_random_machine(the_list):
    ''' This produces a set of numbers in a random order that will become the names_list's indexes.'''
    
    the_new_list = []
    
    # https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range (Two-Bit Alchemist, Apr 3rd, 2014)
    the_random_list = random.sample(range(0, len(the_list)), (len(the_list)))

    # Creates a new list that has all the names but in a different order. Duplicates are checked later.
    for i in range(len(the_list)):
        the_new_list.append(the_list[the_random_list[i]])
    return the_new_list


#--------------------------------------------MAIN CODE----------------------------------------------

def main():
    
    # A welcome message on what to do is produced.
    welcome_message()

    # Names are collected and the 'exit' part at the end is removed.
    names_list = name_collector()    
    names_list.pop(len(names_list)-1)

    # Prints out all the names that are in the list
    for i in range(len(names_list)):
        print(f"\nName number {i+1}: {names_list[i]}")

    # User is asked if they like the list of names presented.
    user_confirm = input("\nAre these names correct? Answer \"y\" if you are happy, anything else if not: ")

    # If the user is not happy with the list, they can enter it in again
    while user_confirm != 'y':
        names_list = name_collector()
        names_list.pop(len(names_list)-1)
        for i in range(len(names_list)):
            print(f"Name number {i}: {names_list[i]}")
        user_confirm = input("Are these now correct? Answer \"y\" if you are happy, anything else if not: ")

    # This hard-reboots the program if only one name is entered. After all, the program can't shuffle one name.
    if len(names_list) < 2:
        print("\n\n-------------Error: Only one name was entered. Restarting...----------------")
        main()

    # A list of randomly-shuffled names is created.
    random_list = the_random_machine(names_list)
    
    # Variables for the upcoming while loop are declared.
    duplicates_checked = False
    shuffle = 0

    # This while loop checks for any matching names from the orginal list to the randomized list.
    # If there's a match, the list is reshuffled again.
    while duplicates_checked != True:
        for i in range(len(random_list)):
            if random_list[i] == names_list[i]:
                print(f"Random {random_list}")
                print(f"Normal {names_list}")
                random_list = the_random_machine(names_list)
                shuffle = shuffle + 1
                print(f"Shuffle number: {shuffle}")
            else:
                duplicates_checked = True

    # Once sorted, every name is paired with the other name, the original name is given a .txt file
    # that will contain that person's secret santa recipient.
    for i in range(len(names_list)):
        file = open(f"{names_list[i]}'s secret santa recipient.txt", 'w')
        file.write(random_list[i])
        file.close()

# A boiler plate. That is all.
if __name__ == '__main__':
    main()

