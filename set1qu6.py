print("Enter the String ")

string=input().lower();
cc=0
for a in string:
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
        cc=cc+1
print('Number of Vowels in',string, 'is',cc)