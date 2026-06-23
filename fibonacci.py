
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

def  febo(n):
    if n==1 or n==2:
        return 1
    else:
        return febo(n-1)+ febo(n-2)
febo(5)
        