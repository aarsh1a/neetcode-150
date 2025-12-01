# sort each of them and compare using the hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numMap = {}         
        for word in strs:
            key = "".join(sorted(word))             
            if key not in numMap:
                numMap[key] = []           
            numMap[key].append(word)       
        return list(numMap.values())