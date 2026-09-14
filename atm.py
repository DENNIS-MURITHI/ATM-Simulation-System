print('=============================')
print('          Dennis ATM         ')
print('=============================')


correct_pin = 1234
balance = 40000

pin = int(input('Enter your pin: '))
if pin == correct_pin:

    print('ATM Menu')
    print('1 check the balance')
    print('2 Withdraw money')
    print('3 Deposit Money')
    print('4 Exit')

    option = int(input('Select an option from the menu: '))
    if option == 1:
        print(f'your balance is {balance}')
    elif option == 2:
        amount = int(input('enter the withdraw amount: '))
        if amount <= balance:
            balance -=amount
            print('withdrawal successful')
            print('your remaining balance is ',balance)
        else:
            print('insufficient balance')
    elif option == 3:
        amount = int(input('Enter deposit money: '))
        balance +=amount
        print('Deposit succesful')
        print('Your balance is ', balance)
else:
    print('wrong pin')


