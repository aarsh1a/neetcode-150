# start and l,r->calculate area and store in maxarea->check l,r and update lower one to next calculate area again and update maxarea if higher
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            usableHeight=min(height[l],height[r])
            width=r-l
            area= usableHeight*width
            if area>maxArea:
                maxArea=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea