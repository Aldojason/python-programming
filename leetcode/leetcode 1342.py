arr=[2,3,4,5,2,3,2,2]
k=3
threshold=3
window_sum=0
count=0
for i in range(k):
    window_sum+=arr[i]
    if window_sum>=threshold*k:
        count+=1
    left=0
for right in range(k,len(arr)):
    window_sum=window_sum-arr[left]+arr[right]
    if window_sum>=threshold*k:
        count+=1
    left+=1
print( count)
        


        