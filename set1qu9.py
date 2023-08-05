print('Enter the nth term to find the array of its factorial series')
num=int(input())
def getFac(num):

    if num<=1 :
        
        return 0
    elif num==2:
        return 1
    else:
        return getFac(num-1)+getFac(num-2)
arr=[]
for i in range(1,num+1):
    arr.append(getFac(i))
print(arr)
