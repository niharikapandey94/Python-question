numbers = [12, 75, 150, 180, 145, 525, 50];
for i in numbers:
    if i>500:
        break
    elif i>150 or i%5!=0:
        continue
    else:
        print(i)