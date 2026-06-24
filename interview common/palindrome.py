def palindrome(text):
    text=text.lower()
    newstring=""
    for ch in text:
        if ch.isalnum():
            newstring+=ch
    left=0
    right=len(newstring)-1
    while left<right:
        if newstring[left]!=newstring[right]:
            return False
        left+=1
        right-=1
    return True
s=input("enter the text:")
print(palindrome(s))