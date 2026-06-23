a=int(input("enter first number:"))
b=int(input("enter second number:"))
op=input("enter operation (+,-,*,/):")
if op=='+':
    print(f"{a}+{b}={a+b}")
elif op=='-':
    print(f"{a}-{b}={a-b}")
elif op=='*':
    print(f"{a}*{b}={a*b}")
elif op=='/':
    if b!=0:
        print(f"{a}/{b}={a/b}")
    else:
        print("division by zero is not possible")
else:
    print("invalid operation")