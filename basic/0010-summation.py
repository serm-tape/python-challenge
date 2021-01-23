'''
Modify sum function to return sum of total number in the list
'''
def sum(numbers):
    #Modify function body here
    return 0

while(True):
    numbers = list(map(lambda n: int(n), input('numbers: ').split()))
    total = sum(numbers)
    print('total:', total)

