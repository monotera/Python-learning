import os
import time


def menu():
    os.system('clear')  # funcion que limpia pantalla
    print("Blacklist agenda")
    print("\tSelect an option")
    print("\t1 - Enter the contact information")
    print("\t2 - Contacts that I like")
    print("\t3 - Contacts that I dislike")
    print("\t4 - Delete a contact")
    print("\t5 - Find a contact")
    print("\t6 - Exit")


phoneBook = []
option = 0


def fillInfo():
    name = input('Name: ')
    number = input('Phone number: ')
    direction = input('Direction: ')
    status = input('Status (1 = friend || 2 = enemy)')
    while status != '1' and status != '2':
        print('Error invalid option')
        status = input('Status (1 = friend || 2 = enemy)')
    dic = {1: name, 2: number, 3: direction, 4: status}
    phoneBook.append(dic)


def friendList():
    for x in phoneBook:
        if x[4] == '1':
            print(x[1], x[2], x[3])


def enemyList():
    for x in phoneBook:
        if x[4] == '2':
            print(x[1], x[2], x[3])


def deleteContact():
    i = 0
    for x in phoneBook:
        if x[4] == '1':
            print(i, ') ', x[1], x[2], x[3], 'Friend')
        else:
            print(i, ') ', x[1], x[2], x[3], 'Enemy')
        i += 1
    if len(phoneBook) > 0:
        index = int(
            input('Insert the number of the contact you want to delete: '))
        try:
            phoneBook.pop(index)
        except:
            print("ERROR!: incorrect value")
    else:
        print('There are no contacts')

def searchContact():
    name = input('Name of the contact to search: ')
    for x in phoneBook:
        if x[1] == name:
            print(x[1], x[2], x[3], x[4])

while option != '6':
    menu()
    option = input('Type the number of the option you want to see: ')
    os.system('clear')
    if option == '1':
        fillInfo()
    elif option == '2':
        friendList()
    elif option == '3':
        enemyList()
    elif option == '4':
        deleteContact()
    elif option == '5':
        searchContact()
    elif option == '6':
        print('Sayoonara!')
    else:
        print('ERROR')
    input("Press enter to continue...")
        
