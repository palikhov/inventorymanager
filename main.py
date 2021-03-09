# dnd inventory system management
# user input characters
characters = []
# print("input character name")
# print(characters)
# user input items

while True:
    print("What do you wanna do? 1 for adding a character. 2 for adding to the inventory of a character. 3 to print the list of characters. 4 for quit")
    user_input = int(input())
    if user_input == 1:
        print("Add character")
        characters.append(input())
        continue
    elif user_input == 2:
        print("What character do you want to add inventory items to?")
    elif user_input == 3:
        print(characters)
    elif user_input == 4:
        print("trash")
    else:
        break


print("done")
