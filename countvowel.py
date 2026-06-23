string=input("enter a string:")
count=0
for i in string:
    if i.lower() in 'aeiou':
        count+=1
print("Number of vowels in the string:", count)