if __name__=="__main__":
    from util import math
    n,m=map(int,input().split())
    list1=[]
    for i in range(n):
        l=list(map(int,input().split()))
        list1.append(l)
    print(math(list1))