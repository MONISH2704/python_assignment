import numpy as np
def det(list1):
    arr1=np.array(list1)
    p=np.linalg.det(arr1)
    return round(p,2)