class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
            if f[i]>1:
                return True
        
        return False
        