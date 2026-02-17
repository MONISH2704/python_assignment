import numpy as np
def calculate(n,m):
    arr=np.array([list(map(int, input().split()))for i in range(n) ])
    arr1=np.min(arr, axis=1)
    print(np.max(arr1))