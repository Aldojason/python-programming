class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        total=0
        for row in grid:
            left=0
            right=len(row)-1
            count=0
            while left<=right:
                mid=left+(right-left)//2
                if row[mid]<0:
                    count=len(row)-mid
                    right=mid-1
                if row[mid]>=0:
                    left=mid+1
            total+=count
        return total
                


        