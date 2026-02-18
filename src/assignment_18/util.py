l=[]
def list1(user_input):
    if user_input[0]=='insert':
        l.insert(int(user_input[1]),int(user_input[2]))
    elif user_input[0]=='print':
        print(l)
    elif user_input[0]=='remove':
        l.remove(int(user_input[1]))
    elif user_input[0]=='append':
        l.append(int(user_input[1]))
    elif user_input[0]=='sort':
        l.sort()
    elif user_input[0]=='pop':
        l.pop()
    elif user_input[0]=='reverse':
        l.reverse()
        
    
