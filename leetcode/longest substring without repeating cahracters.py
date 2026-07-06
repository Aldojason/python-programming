s = "abcabcbb"
left=0
right=0
seen=set()
longest=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    longest = max(longest, right - left + 1)
    
print(longest)
