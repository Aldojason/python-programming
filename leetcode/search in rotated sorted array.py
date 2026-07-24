a=[3,4,5,1,2,3]
target=4
left=0
right=len(a)-1
while left<=right:
    mid=left+(right-left)//2
    if a[mid]==target:
        print(mid)
    if a[left]<a[mid]:
        if a[left]<=target<a[mid]:
            right=mid-1
        else:
            left=mid+1
    else:
        if a[mid]<target<=a[right]:
            left=mid+1
        else:
            right=mid-1
