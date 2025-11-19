'''
-----------------------------------------------------------------------------
Program Name: Bank machine
Program Description: 

-----------------------------------------------------------------------------
References:
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

None

-----------------------------------------------------------------------------

Known bugs:

None that are known of

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level 4+ because I added much more than was needed and made the code in very short amount
of lines

 Level 3 Requirements Met:
• 4 options
• Overdraw condition
• Login
• 
•  
• 

Features Added Beyond Level 3 Requirements:
• Colored words
•  Sign up option
•  Ascii art
•  Option to refuse withdrawl if negative
•  
• 
-----------------------------------------------------------------------------
'''
#I had to search up what the colours were
import random
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'
print('''
██████   █████  ███    ██ ██   ██     ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██   ██ ██   ██ ████   ██ ██  ██      ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██████  ███████ ██ ██  ██ █████       ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██   ██ ██   ██ ██  ██ ██ ██  ██      ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
██████  ██   ██ ██   ████ ██   ██     ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                                                                              
                                                                                              ''')
#Login loop
accepted={"swindrunner":"1234",'istormrage':'abcd','tpgallywix':'qwerty'}
while True:
    choice=input('1:Sign up or 2:Sign in: ')
    if choice=='2':
        user=input("Input username: ")
        password=input("Input password: ")
        if user in accepted.keys() and accepted[user]==password:
            print(f'{GREEN}Correct login!{RESET}')
            break
        else:
            print(f'{RED}Incorrect login, try again{RESET}')
    elif choice=='1':
        name=input('Enter user: ')
        password2=input('Enter password: ')
        print(f'{GREEN}Added User to database!{RESET}')
        accepted[name]=password2
    else:
        print(f'{RED}Please enter valid input.{RESET}')
        
tips=['Wait 24 hours before buying impulse items.','Cook at home instead of ordering takeout.','Buy store brands instead of name brands.','Cancel subscriptions you do not use.','Track every dollar you spend this week.']
balance=random.randint(500,2500)
while True:
    action=input(f"Enter number: {BLUE}1:Display Balance{RESET}, {YELLOW}2:Withdraw{RESET}, {CYAN}3:Deposit{RESET}, {RED}4:Exit{RESET}, {MAGENTA}5:Money Tips{RESET}: ")
    #show balance
    if action=='1':
        print('Your balance:'+str(balance))
    #Withdraw assuming the fee applies for the up to -500 rule
    elif action=='2':
        try:
            #Try to catch errors
            num=input('Enter withdraw amount: ')
            num=int(num)
            if abs(num)!=num:
                print(f'{RED}Input only positive number in withdraw.{RESET}')
        except:
            print(f'{RED}Input valid number please.{RESET}')
            continue
        #Calculate what balance will be
        potential_balance = balance-num
        if potential_balance<0:
            fee=num*0.2
            final_result=potential_balance-fee
            overdraft=True
        else:
            fee=0
            final_result=potential_balance
            overdraft=False
        #Balance over -500
        if final_result<-500:
            print(f"{RED}Unable to withdraw that much, balance will be over -500{RESET}")
        #Balance negative
        elif overdraft:
            print(f"{YELLOW}WARNING: This will result in an overdraft.{RESET}")
            print('A 20 percent fee of $'+str(fee)+' will be added.')
            print('Your new balance will be: '+str(final_result))
            choice= input(f'Do you want to continue? {GREEN}Yes{RESET}/{RED}No{RESET}: ')
            if choice.lower() in ['yes', 'y']:
                balance= final_result
                print('Your new balance is: '+str(balance))
            else:
                print(f'{RED}Withdraw cancelled.{RESET}')
        #Balance positive
        else:
            balance=final_result
            print('Your new balance is: '+str(balance))
    #Deposit
    elif action =='3':
        try:
            num2=int(input('How much are you depositing?'))
        except:
            print(f'{RED}Input valid number please.{RESET}')
            continue
        print('Your new balance is: '+str(balance+num2))
        balance+=num2
    #Exit
    elif action=='4':
        print(f"{GREEN}Thank you for using our bank!{RESET}")
        break
    #Tips
    elif action=='5':
        print(tips[random.randint(0,4)])


