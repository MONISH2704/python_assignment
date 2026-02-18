if __name__=="__main__":
    from util import list1
    n=int(input())
    for i in range(n):
        user_input=input().split()
        print(list1(user_input))
