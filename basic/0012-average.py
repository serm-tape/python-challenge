'''
Modify avg function to return average of number in the list
'''
def avg(numbers):
    #Modify function body here
    return 0

while(True):
    numbers = list(map(lambda n: int(n), input('numbers: ').split()))
    result = avg(numbers)
    print('avg:', result)

