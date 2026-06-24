class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        for k,j in f.items():
            if j==1:
                return k