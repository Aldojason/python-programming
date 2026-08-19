class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        first=-1
        second=-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                first=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1   
            else:
                left=mid+1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                second=mid
                left=mid+1
            elif nums[mid]>target:
                right=mid-1   
            else:
                left=mid+1
        
        return [first,second]


