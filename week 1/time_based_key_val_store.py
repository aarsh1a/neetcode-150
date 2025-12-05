# hashmap with key and value as list with value and timstamp return normally unless somethng doesnt match to fin lowest close use binary search 
class TimeMap:

    def __init__(self):
        self.numMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.numMap:
            self.numMap[key]=[]
        self.numMap[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.numMap:
            return ""
        arr=self.numMap[key]
        l=0
        r=len(arr)-1
        res=""
        while l<=r:
            mid=(l+r)//2
            if arr[mid][0]<=timestamp:
                res=arr[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
