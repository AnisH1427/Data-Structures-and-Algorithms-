#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.
from scipy.optimize._lsq.common import print_iteration_nonlinear


# capitalizeFirst Solution

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 


s=["Anish","Sulochana"]
print(s[0][1:])
print(s[0][0]+s[0][1:])

print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']