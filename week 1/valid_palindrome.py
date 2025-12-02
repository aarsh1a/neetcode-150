#convert everythign to lowercase, remove spaces and extras, read from both sides and equate
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean=""
        for ch in s:
            if ch.isalnum():
                clean +=ch
        l=0
        r=len(clean)-1
        while l<r:
            if clean[l]!=clean[r]:
                return False
            l+=1
            r-=1
        return True