def word(n):
    word_count={}
    appear=[]
    for _ in range (n):
        word=input()
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
            appear.append(word)
    output = ""
    output += str(len(appear)) + "\n"
    output += " ".join(str(word_count[word]) for word in appear)

    return output