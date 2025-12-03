# set up a count hashmap with the count of types of chars in string with their frequencies and keep track fo the most frequent element 
#move r->> and keep checking if windowlen-count[mostfreq]<=k if yes make window len the res otherwise l++ make window shorter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        numMap={}
        l=0
        maxCount=0
        best=0
        for r,ch in enumerate(s):
            numMap[ch]=numMap.get(ch,0)+1
            if numMap[ch]>maxCount:
                maxCount=numMap[ch]
            while (r-l+1)-maxCount>k:
                numMap[s[l]]-=1
                l+=1
            if r-l+1>best:
                best=r-l+1
        return best