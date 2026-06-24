#left rotation
# a=[1,2,3,4,5]
# r=3
# for _ in range(r):
#     first=a[0]
#     for j in range(1,len(a)):
#         a[j-1]=a[j]
#     a[len(a)-1]=first
# print(a)

# right rotation
a=[1,2,3,4,5]
r=2
for _ in range(r):
    last=a[len(a)-1]
    for j in range(len(a)-1,0,-1):
        a[j]=a[j-1]
    a[0]=last
print(a)