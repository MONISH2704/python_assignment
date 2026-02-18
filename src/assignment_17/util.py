from itertools import combinations

def iter(n,list1,k):
    comb_items=list(combinations(list1,k))
    count=0
    for comb in comb_items:
        if 'a' in comb:
            count+=1
    result=count/len(comb_items)
    return round(result,3)