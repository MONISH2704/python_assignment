def merge(string,k):
    start=0
    end=k

    while end <= len(string):
        temp=string[start:end]
        result=list(set(list(temp)))
        print(' '.join(result))
        start+=k
        end+=k
