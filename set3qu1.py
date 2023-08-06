input=[("John", 25), ("Jane", 30)]
bag='';
for j in input:
    bag+=str(j[0])+' is '+str(j[1])+' years old.'
print(bag)