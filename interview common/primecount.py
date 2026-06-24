num=int(input("enter a number:"))
count=0
for i in range(2,num+1):
    prime=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=0
            break
    if prime==1:
        count+=1
print(f"prime numbers upto {num} is:", count)
