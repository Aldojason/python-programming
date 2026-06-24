lst=[2,3,4,5,6,7]
target=int(input("enter a number to search:"))
found=False
for i in range(len(lst)):
    if lst[i]==target:
        print("element is found at the index:",i)
        found=True
        break
if not found:
    print("element is not in the list")