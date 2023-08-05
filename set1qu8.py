print("Enter the number to get Factorial of it")

num=int(input())
p=1
for i in range(1,num+1):
    p*=i
print('The factorial of given number is',p)