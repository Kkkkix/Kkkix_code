'''0.尝试利用字典的特性编写一个通讯录程序吧！'''

print('|---Welcome to Kkkix‘s address book program ---|')
print('|---------1.Query contact information ---------|')
print('|---------2.Add a new contact -----------------|')
print('|---------3.Delete a contact ------------------|')
print('|---------4.Quit the program ------------------|')
dict = {'w':135}

while True:

    comm_code = input('please input your command code:')
    if  comm_code == '1':
        name = input('please enter the name of contact:')
        if name in dict.keys():
            print(name,end=' : ')
            print(dict[name], end='\n\n')
        else:
            print('The name you found is not in the address book.')
            print('Please try again\n')
            continue

    elif comm_code == '2':
        name = input('please enter the name of contact:')
        if name in dict.keys():
            print('The name you entered is already in the address book: -->> %s : %d' % (name,dict[name]))
            while True:
                ans = input('Are you sure you want to change the existing contact (Yes/No): ')
                if ans == 'Yes':
                    phone_num = int(input('Please input the phone number of contact: '))
                    print('')
                    dict[name] = phone_num
                    break
                elif ans == 'No':
                    print('')
                    break
                else:
                    continue
        else:
            phone_num = int(input('Please input the phone number of contact: '))
            print('')
            dict[name] = phone_num

    elif comm_code == '3':
        print("This function haven't been done!!!!")
    elif comm_code == '4':
        break
    else:
        print("The command code you entered is not exist.")
        print()
        continue

print("|---Thanks for using the Kkkkix's address book---|")
