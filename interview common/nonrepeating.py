def nonrepeat(str):
    freq={}
    for char in str:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    for char in str:
        if freq[char]==1:
          return char
        
    return -1
s=input("enter the string:")
print(nonrepeat(s))