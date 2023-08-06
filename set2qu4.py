str1 = 'PyNaTive'
bag1=''
bag2=''
for a in str1:
    if a.islower():
        bag1+=a
    else:
        bag2+=a
print(bag1+bag2)
