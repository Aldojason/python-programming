binary=input("enter the binary number:")
decimal=0
for i in range(len(binary)):
    digit=binary[-(i+1)]
    if digit=='1':
        decimal=decimal+(2**i)
print("decimal number:",decimal)