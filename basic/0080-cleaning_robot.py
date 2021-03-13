'''
Modify robot function to return the final position of the robot
W: move up
A: move left
S: move right
D: move down 
starting from coordiate (0,0)

Input: WWWAASD
Output: (-1, 2)
'''

def exec(commands):
    position = (0, 0)
    #Modify function body here

    return position

while(True):
    commands = list(input('commands: '))
    result = exec(commands)
    print('Final position:', result)

