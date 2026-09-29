s=input("enter string:")
if len(s)>=8 and any(i.isupper() for i in s) and any(i.islower() for i in s) and any(i.isdigit() for i in s):
    print("strong")
else:
    print("weak")