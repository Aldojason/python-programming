a=[10,23,54,34,64,35]
first=float('-inf')
second=float('-inf')
for i in a:
    if i>first:
        second=first
        first=i
    elif i<first and i>second :
        second=i
print(second)
