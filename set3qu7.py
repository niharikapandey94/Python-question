bag=""
for i in range(1,101):
    if i%3==0 and i%5==0:
        bag+="FizzBuzz "
    elif i%3==0:
        bag+='Fizz '
    elif i%5==0:
        bag+='Buzz '
    else :
        bag+=str(i)+" "

print(bag)