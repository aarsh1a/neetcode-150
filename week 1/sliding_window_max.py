#brute just find max and display for each window but tle
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        l=0
        r=k-1
        while r<n:
            currMax=nums[l]
            for i in range(l+1,r+1):
                if nums[i]>currMax:
                    currMax=nums[i]
            res.append(currMax)
            l+=1
            r+=1
        return res
    
#optimized in using DEqueue