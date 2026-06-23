a=[12,53,32,44,55]
target=32
found=False
for i in range(0,len(a)):
    if a[i]==target:
        found=True
        print(i)
        break
if found:
    print("exist")
else:
    print("not exist")
