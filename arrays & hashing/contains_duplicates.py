class Solution(object):
    def containsDuplicate(self, nums):
        new=set(nums)
        if len(new) < len(nums):
            return True
        else:
            return False        