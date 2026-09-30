n=int(input("enter no.of items"))
a=[]
b=[]
for i in range(n):
    item_name=input("enter iteam name:")
    price_unit=int(input("enter 1 unit price:"))
    quantity=int(input("enter quantity:"))
    cost=price_unit*quantity
    b.append(cost)
    a.append([item_name,price_unit,quantity])
total=0
for i in b:
    total+=i
if total>1000:
    total=total-total/10
GST=total*0.05
final_amount=total+GST
print("===============================")
for i in a:
    print(i   )
for j in b:
    print( j)
print("===============================")
print("total=",total)
if total>1000:
    print("discount= 5%")
print("GST=",GST)
print("final_total=",final_amount)
