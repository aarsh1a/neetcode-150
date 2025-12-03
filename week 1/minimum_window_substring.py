# needmap for char in t and their count and a window 
# map of chars in the window update each time moving r to 
# the right and everytime condition satisfied against needmap, have++ 
# when have and need equal reduce using l++ update  and switch again till smallest window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        needMap = {}
        for ch in t:
            needMap[ch] = needMap.get(ch, 0) + 1
        
        windowMap = {}
        have = 0
        need = len(needMap)
        
        resL = 0
        resR = 0
        resLen = float("inf")
        
        l = 0
        for r in range(len(s)):
            ch = s[r]
            windowMap[ch] = windowMap.get(ch, 0) + 1
            
            if ch in needMap and windowMap[ch] == needMap[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resL = l
                    resR = r
                    resLen = r - l + 1
                
                leftChar = s[l]
                windowMap[leftChar] -= 1
                if leftChar in needMap and windowMap[leftChar] < needMap[leftChar]:
                    have -= 1
                l += 1
        
        if resLen == float("inf"):
            return ""
        return s[resL:resR+1]