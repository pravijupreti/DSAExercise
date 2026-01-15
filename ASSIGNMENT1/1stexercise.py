arr = input("Enter the string : ")
newarr = []
for i in range(len(arr)):
    pos = 0
    while pos < len(newarr) and newarr[pos] <arr[i]:
        pos += 1
    newarr.insert(pos,arr[i])
print(newarr)