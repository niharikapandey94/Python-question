[a,b]=[input('Enter the First Number'),input('Enter the Second Number')]
try:
    print('The result of division is '+str(int(a)/int(b)))
except ZeroDivisionError:
    print("0 can't be the divisor")