a=[1,0,4,5,0,3]
left = 0
for i in a:
    if i != 0:
       a[left] = i
       left += 1
for i in range(left,len(a)):
    a[i]=0
print(a)
