'''
Modify grading function to return grade 
'''
grade_range = [50, 60, 70, 80]
def grading(score):
    #Modify function body here    
    return 'F'

while(True):
    score = int(input('score: '))
    grade = grading(score)
    print('grade:', grade)

