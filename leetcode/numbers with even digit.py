a=list(map(int, input("enter values:").split()))
sum=0
for i in a:
    length=len(str(i))
    if length%2==0:
        sum+=1
print(sum)