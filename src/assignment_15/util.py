def calculate(n,m,list1,a,b):
    happiness=0
    for i in list1:
        if i in a:
            happiness+=1
        elif i in b:
            happiness-=1
    return happiness