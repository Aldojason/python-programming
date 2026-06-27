a = [2,1,5,1,3,2]
k = 3
window_min=0
minnum=float('-inf')
for i in range(k):
    window_min+=a[i]
minnum=window_min
for j in range(k,len(a)):
    window_min=window_min+a[j]-a[j-k]
    if window_min<minnum:
        minnum=window_min
print(minnum)
