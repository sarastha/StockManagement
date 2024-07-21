# Defining a function to overwrite the txt file which accepts the list and dictionary as its parameters
def over_writing_sale (listed_troops, dictionary_troops):
    # Assigning the returned list from read laptop to a new variable
    list_data = listed_troops
    # Assigning the returned dictionary from sale notice to a new variable
    dictionary_data = dictionary_troops

    # Examining the index of the list and then subtracting from its respective key of the dictionary
    for keys in dictionary_data.keys():
        for i in range(len(list_data)):
            if str(keys) == list_data[i][0]:
                list_data[i][4] = str(int(list_data [i][4]) - int(dictionary_data[keys]))

    # Displaying of the new updated list after reducing the amount of  laptop stock
    print()
    print("The new updated list are as follows: ")
    for element in list_data:
        print(element)

    # File writing to update the quantity of the laptop stock after selling
    files = open("laptop.txt", "w")
    for each in list_data:
        files.write(str(",".join(each)))
        files.write("\n")
    files.close()
    return

# Defining a function to overwrite the txt file which accepts the list and dictionary as its parameters
def over_writing_purchase (listed_troops, dictionary_troops):
    # Assigning the returned list from laptop read to a new variable
    list_data = listed_troops
    # Assigning the returned dictionary from sale notice to a new variable
    dictionary_data = dictionary_troops

    # Examining the index of the list and then adding with its respective key of the dictionary
    for keys in dictionary_data.keys():
        for i in range(len(list_data)):
            if str(keys) == list_data[i][0]:
                list_data[i][4] = str(int(list_data [i][4]) + int(dictionary_data[keys]))

    # Displaying of the new updated list after reducing the amount of  laptop stock
    print()
    print("The new updated list is as follows: ")
    for element in list_data:
        print(element)

    # File writing to update the quantity of the laptop stock after returning
    files = open("laptop.txt", "w")
    for each in list_data:
        files.write(str(",".join(each)))
        files.write("\n")
    files.close()
    return
