#check notebook
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        res=0
        heights.append(0)
        for i,x in enumerate(heights):
            while st and x<heights[st[-1]]:
                H=heights[st.pop()]
                W=i if not st else i-st[-1]-1
                res=max(res,H*W)
            st.append(i)
        return res