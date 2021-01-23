'''
Modify atm function to return how many bank notes needed for the amount
Available bank note are: 1000, 500, and 100
Returning ranged from the largest note to smallest one

input: 3700
output: (3, 1, 2)
'''

def withdraw(amount):
    #Modify function body here

    return (0, 0, 0)

while(True):
    amount = int(input('amount: '))
    result = withdraw(amount)
    print('Returned notes:', result)

