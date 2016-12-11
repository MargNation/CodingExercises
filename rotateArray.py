# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] 
# is rotated to [5,6,7,1,2,3,4].

# Exercise discovered on www.programcreek.com

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def rotateArray(arr, k):
    
    returnArray = []
    
    for i in range(len(arr)):
        returnArray.append(arr[(len(arr) - k + i) % len(arr)])
    
    return returnArray

print rotateArray(testArray, 3)
