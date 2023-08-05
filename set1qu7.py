print('Enter the number to check for Prime')
num=int(input())
cc=0
for i in range(1,num+1):
    if num%i==0:
        cc=cc+1
if cc==2:
    print(num,'is Prime')
else:
    print(num,'is not Prime')