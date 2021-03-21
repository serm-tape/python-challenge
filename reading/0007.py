'''
What should be output of this program?
'''
a = [1, 7, 16, 23]
b = [7, 9, 16]
c = []
for i in a:
    for j in b:
        print(i)
        print(j)
        if i == j:
            c.append(i)
        print(c)


