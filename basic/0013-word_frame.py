'''
Modify frame fuction to add frame to the word
First parameter will be the word to add frame
Second parameter will be table angle
Thrid parameter is horizontal border
and Fourth parater is vertical border

input: Hello, world
input: +
input: -
input: |
output: 
+------------+
|Hello, world|
+------------+

'''
def frame(word):
    #Modify function body here    
    return word

while(True):
    word = input('word: ')
    angle = input('angle: ')
    hBorder = input('hBorder: ')
    vBorder = input('vBorder: ')

    print(frame(word))
