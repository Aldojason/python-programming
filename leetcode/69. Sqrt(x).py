class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while left<=right:
            mid=left+(right-left)//2
            if mid*mid>x:
                right=mid-1
            if mid*mid<=x:
                sqr=mid
                left=mid+1
        return sqr
        
        

        