arr = [1,2,3,4,5]
sum = 0
for i in range(len(arr)-1):
    sum = sum+arr[i]

print(sum)

arr1 = []
arr1 = arr
print(arr1)
    
arr2 = [1,2,3,4,5] #array of integers
arr3 = [1.0,2.0,3.0,4.0,5.0] #array of float
arr4 = ["hello","world","mtalkz"] #array of string

def mergeTwoArray(arr5,arr6):
    i = 0
    j = 0
    len1 = len(arr5)
    len2 = len(arr6)
    arr7 = []
    while((i < len1) and (j < len2)):
        if(arr5[i] < len1):
            arr7.append(arr5[i])
            i += 1
        else:
            arr7.append(arr6[j])
            j += 1
        
    return arr7

arr5 = [1,2,3,4,5]
arr6 = [6,7,8,9,10]
arr7 = mergeTwoArray(arr5,arr6)
print(arr7)

print(arr5)

a = [1,2,3,4,5]
b = [4,5,6,7,8]


c = mergeTwoArray(a,b)
s = set(c)
print(s)
