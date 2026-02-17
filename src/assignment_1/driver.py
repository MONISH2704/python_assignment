if __name__=="__main__":
    from util import runner
    n=(input("enter numbers: "))
    arr=map(int,n.split(','))
    print(runner(arr))