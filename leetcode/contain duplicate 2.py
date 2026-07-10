def containduplicate(nums,k):
    seen=set()
    left=0
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
        if len(seen)>k:
            seen.remove(nums[left])
            left+=1
    return False
print(containduplicate(nums=[1,2,3,1,4,5],k=3))
      