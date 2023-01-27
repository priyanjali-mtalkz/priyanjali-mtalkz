word = "hello"
i = len(word)-1
newWord = ""
for j in word:
    newWord += (word[i])
    i = i-1
    
print(newWord)

x = 5
print(type(x))
    
arr = [1,2,3,4,5]
print(len(arr))

del(arr[:len(arr)])
print(len(arr))

