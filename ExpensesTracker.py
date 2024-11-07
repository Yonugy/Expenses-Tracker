wallet=0
bank=0
income=float(input('How much is your income? RM'))
wallet+=income
print('Your income of RM%s is now in your wallet.' %str(format(income,'g')))
save=float(input('How much money do you want to save in bank? RM'))
while save>wallet:
    print('You cannot save an amount more than you got in your wallet!')
    save=float(input('How much money do you want to save in bank? RM'))
print(format(save/income*100,'.2f')+'% from your income saved in your bank.')
bank+=save
wallet-=save
print('-'*20)
print('Your current balance:')
print('Wallet: RM%.2f' %wallet)
print('Bank: RM%.2f' %bank)
print('-'*20)
expenses_info=[]
expenses_price=[]
info=0
price=0
def InputExpenses():    #Action 1
    global wallet
    info=input('Please input the use of the expense: ')
    price=float(input('Please input the price of the expense: RM'))
    while price>wallet:
        print('You cannot use an amount more than you got in your wallet!')
        price=float(input('How much money do you want to save in bank? RM'))
    expenses_info.append(info)
    expenses_price.append(price)
    print('RM%.2f used for %s.'%(price,info))
    wallet-=price

def PutWallet():        #Action 2
    global wallet
    put=float(input('Please input the amount you put in wallet: RM'))
    print('RM%.2f putted in wallet.'%put)
    wallet+=put

def SaveBank():         #Action 3
    global wallet
    global bank
    save=float(input('Please input the amount you want to save to bank: RM'))
    while save>wallet:
        print('You cannot save an amount more than you got in your wallet!')
        save=float(input('Please input the amount you want to save to bank: RM'))
    print('RM%.2f saved in to bank.'%save)
    wallet-=save
    bank+=save

def Withdraw():         #Action 4
    global wallet
    global bank
    withdraw=float(input('Please input the amount you want to withdraw from bank. RM'))
    while withdraw>bank:
        print('You cannot withdraw an amount more than you got in your bank!')
        withdraw=float(input('Please input the amount you want to withdraw from bank. RM'))
    print('RM%.2f withdraw from bank.'%withdraw)
    bank-=withdraw
    wallet+=withdraw

def CheckBalance():     #Action 5
    print('Your current balance:')
    print('Wallet: RM%.2f' %wallet)
    print('Bank: RM%.2f' %bank)

def CheckExpenses():    #Action 6
    for i in range(len(expenses_info)):
        print(str(i+1)+')',expenses_info[i],'RM'+str(expenses_price[i]))

while True:
    print('1) Input expense.')
    print('2) Put money in to wallet.')
    print('3) Save money from wallet in to bank.')
    print('4) Withdraw money from bank.')
    print('5) Check currect balance.')
    print('6) Check all expenses.')
    print('7) Exit.')
    choice=input('Please choose your action: ')
    print('-'*20)
    if choice=='1':
        InputExpenses()
    elif choice=='2':
        PutWallet()
    elif choice=='3':
        SaveBank()
    elif choice=='4':
        Withdraw()
    elif choice=='5':
        CheckBalance()
    elif choice=='6':
        CheckExpenses()
    elif choice=='7':
        break
    else:
        print('Please choose action by typing number 1, 2, 3, 4, 5, 6 or 7.')
    print('-'*20)
print('Thanks you. Have a nice day.')
