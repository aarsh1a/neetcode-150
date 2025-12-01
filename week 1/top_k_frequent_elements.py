# add frequency of each num to the hashmap and sort it in descending order, then pull till k value and print
# lambda is helper function used when sorting instead of writing full func seperately -> key=lambda something= whatever part you want to sort by
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            if num in numMap:
                numMap[num]+=1
            else:
                numMap[num]=1
        sortedItems= sorted(numMap.items(),key=lambda item:item[1],reverse=True)
        result=[]
        for i in range(k):
            result.append((sortedItems[i][0]))
        return result 