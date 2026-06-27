nums=[1,2,3,4,5,6]
target=5
f={}
for i,num in enumerate(nums):
    compliment=target-num
    if compliment in f:
         print(f[compliment],i)
    else:
        f[num]=i

            


        