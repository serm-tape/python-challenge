'''
Modify tournament function to return the list of time of racer who pass the qualification
In rancing competition, there is a qualification round to let every participants run in the track
To pass the qualification racer need to beat the average time of all participant

input: list of time used (in seconds)
output: list oft time that beat the average

input: 130 140 150
output: [130, 140]
'''

def qualify(time_list):
    #Modify function body here

    return time_list

while(True):
    time_list = list(map(lambda t: int(t), input('time: ').split()))
    result = qualify(time_list)
    print('Qualified: ', result)

