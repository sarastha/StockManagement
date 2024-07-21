# Defining a function to read the details of a file and store it on a two dimensional list
def read_laptop():
    # Opening of the file that contains the information about the laptops
    file = open("laptop.txt", "r")
    # Use of readlines function in order to store the details on a list
    files = file.readlines()
    list_data = []
    # Appending all the details of the laptop on a new list
    for line in files:
        list_data.append(line.replace("\n", "").split(","))
    file.close()
    # Display of all the details of the laptop in an appropriate matter in order to make it user friendly
    print()
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" \t\t\t\t\t\t\t\tSara Electronics ")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("     ID          Laptop_Name             Company         Price       Quantity     Processor      Graphics")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(list_data)):
        print("     " + list_data[i][0] + "\t\t" + list_data[i][1] + "\t\t" + list_data[i][2] + "\t\t" + "$" + list_data[i][3] + "\t\t" + list_data[i][4] + "\t" + list_data[i][5]+"\t"+ list_data[i][6])
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    # It returns the list that stored the details of the laptop on the 2D list
    return list_data

read_laptop()
