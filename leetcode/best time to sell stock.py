a=[7,8,9,3,6,1,4]
left=0
diff=0
max_num=0
for right in range(1,len(a)):
    if a[left]>a[right]:
        left=right
        right+=1
    else:
        diff=a[right]-a[left]
        if diff>max_num:
            max_num=diff
print(max_num)  