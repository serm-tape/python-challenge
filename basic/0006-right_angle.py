'''
Modify isRight function to return True when given number is right-angle triangle
C^2 = A^2 + B^2
'''
def isRight(x, y, z):
    #Modify function body here
    return False

while(True):
    numbers = list(map(lambda n: int(n), input('numbers: ').split()))
    result = isRight(numbers[0], numbers[1], numbers[2])
    print('result:', result)

