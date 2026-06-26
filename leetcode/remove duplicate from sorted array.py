a=[1,2,2,3,3,3,4,4]
left=0
right=1
while right<len(a):
    if a[left]!=a[right]:
        a[left+1]=a[right]
        left+=1
        right+=1
    else:
        right+=1
print(left+1)