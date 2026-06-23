first=input("enter string one:")
second=input("enter string two:")
first=first.lower().replace(" ","")
second=second.lower().replace(" ","")
freq1={}
freq2={}
for ch in first:
    if ch in freq1:
        freq1[ch]+=1
    else:
        freq1[ch]=1
for ch in second:
    if ch in freq2:
        freq2[ch]+=1
    else:
        freq2[ch]=1
if freq1==freq2:
    print("anagram")
else:
    print("not anagram")


""" s1="jason"
s2="najso"
f={}
f1={}
if len(s1)!=len(s2):
    print("not anagram")
else:
    for i in s1:
        f[i]=f.get(i,0)+1
    for j in s2:
        f1[j]=f1.get(j,0)+1
if f==f1:
    print("anagram")
else:
    print("not anagram") """














