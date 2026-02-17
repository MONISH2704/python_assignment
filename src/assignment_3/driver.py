if __name__=="__main__":
    from util import mutate
    string=input("enter string:")
    i,c=input().split()
    print(mutate(string,int(i),c))