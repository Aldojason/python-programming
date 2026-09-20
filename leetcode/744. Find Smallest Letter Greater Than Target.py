class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left=0
        right=len(letters)-1
        mini=-1
        while left<=right:
            mid=left+(right-left)//2
            if letters[mid]>target:
                mini=letters[mid]
                right=mid-1
            if letters[mid]<=target:
                left=mid+1
        if mini!=-1:
            return mini
        else:
            return letters[0]
