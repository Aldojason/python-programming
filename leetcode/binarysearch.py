a=[1,2,3,4,5,6,7]
target=5
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if target==a[mid]:
        print(mid)
    if target>a[mid]:
        left=mid+1
    else:
        right=mid-1
