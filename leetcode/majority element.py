class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        max=0
        for j,k in f.items():
            if k>max:
                max=k
                ans=j
        return ans