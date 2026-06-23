num=int(input("Enter a number: "))
number=str(num)
numlen=len(number)
armstrong_sum=0
for i in number:
    armstrong_sum+=int(i)**numlen
if armstrong_sum==num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")