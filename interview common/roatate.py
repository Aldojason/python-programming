# a=[1,2,3,4,5]
# last=a[len(a)-1]
# for i in range(len(a)-1,0,-1):
#     a[i]=a[i-1]
# a[0]=last
# print(a)

a=[1,2,3,4,5]
first=a[0]
for i in range(1,len(a)):
    a[i-1]=a[i]
a[len(a)-1]=first
print(a)

