'''
An anagram is a word formed by rearranging the letters of a different word. 
contstraints being 10^4 shows no brute force solution online o(n*m) or o(n log n).
    -hashmap(bruteforce)
    without sortign the strings
    use array of size 26 and count frequency of each char and then make the hashmap.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())