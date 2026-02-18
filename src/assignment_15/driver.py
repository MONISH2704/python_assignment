if __name__=="__main__":
    from util import calculate
    n,m=list(map(int,input().split()))
    list1=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(calculate(n,m,list1,a,b))