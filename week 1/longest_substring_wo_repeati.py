# l and r parse through and keep adding r in hashmap until duplicate->remove from the left till no duplicate then calculate window size update maxLen if needed
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet=set()
        l=0
        maxLen=0
        for r in range(len(s)):
            while s[r] in numSet:
                numSet.remove(s[l])
                l+=1
            numSet.add(s[r])
            window=r-l+1
            maxLen=max(window,maxLen)
        return maxLen