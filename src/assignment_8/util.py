from collections import namedtuple
def average(n,feilds):
    total=0
    for i in range(n):
        students=namedtuple('i',feilds)
        MARKS, CLASS, NAME, ID=input.split()
        i=students(MARKS, CLASS, NAME, ID)
        total+=i.MARKS  
    return total/n