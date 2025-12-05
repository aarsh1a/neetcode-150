#make a array where last is max value of array run ninary search on it  use math.ceil() to round up th enumber of hours of eating
# check for each k if less than h run search on lower half otherwise upper half again 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res =r
        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+= math.ceil(p/k)
            if hours <=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
