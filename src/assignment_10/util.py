import numpy as np

np.set_printoptions(legacy='1.13')

def math(a):
    A1=np.array(a)
    print(np.floor(A1))
    print(np.ceil(A1))
    print(np.rint(A1))