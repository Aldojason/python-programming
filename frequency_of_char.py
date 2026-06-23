a=input("enter a string:")
word=a.lower()
sen=word.split()
b={}
for i in sen:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)