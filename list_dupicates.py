lst=(input("Enter numbers separated by spaces: ")).split()
seen=set()
a=[]
for num in lst:
    if num not in seen:
        a.append(num)
        seen.add(num)
print(a)
    
