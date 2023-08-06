arr=[2, 7, 11, 15]
k=9
fl=False
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if i!=j and arr[i]+arr[j]==k:
            print(i,j)
            fl=True
            break
    if fl:break
