import numpy as np
def math(list1):
    arr1=np.array(list1)
    print(np.mean(arr1,axis=1))
    print(np.var(arr1,axis=0))
    print(np.std(arr1))