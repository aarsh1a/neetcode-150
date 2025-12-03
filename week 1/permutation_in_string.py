#dont like this q somethign i did
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:return False
        need=[0]*26
        window=[0]*26
        for ch in s1:
            need[ord(ch)-97]+=1
        for i,ch in enumerate(s2):
            window[ord(ch)-97]+=1
            if i>=n1:
                window[ord(s2[i-n1])-97]-=1
            if window==need:
                return True
        return False