s=input("enter username:")
if len(s)>=5 and s.isalnum() and " " not in s:
    print("valid username")
else:
    print("invalid username")