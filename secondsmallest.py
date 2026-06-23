a=[10,23,54,34,64,35]
smallest=float('inf')
second_smallest=float('-inf')
for i in a:
    if i<smallest:
        second_smallest=smallest
        smallest=i
    elif i>smallest and i<second_smallest:
        second_smallest=i
print(second_smallest)