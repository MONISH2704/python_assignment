if __name__=="__main__":
    from util import det
    n=int(input())
    list1=[]
    for i in range(n):
        l1=list(map(float,input().split()))
        list1.append(l1)
    print(det(list1))