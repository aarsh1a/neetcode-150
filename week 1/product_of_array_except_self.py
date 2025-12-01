#brute -> start product, set i, skip i, them multiply everything except i and stor eit in output array but this is o(n2)
#result array will be product of left side of * product of right sid eof i , compiles in o(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        beforei=1
        for i in range(n):
            result[i]=beforei
            beforei *= nums[i]
        afteri=1
        for i in range(n-1,-1,-1):
            result[i]*=afteri
            afteri *= nums[i]
        return result