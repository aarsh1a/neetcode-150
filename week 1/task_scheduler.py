#dont get it 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for t in tasks:
            freq[t]=freq.get(t,0)+1

        heap=[-c for c in freq.values()]
        heapq.heapify(heap)

        time=0

        while heap:
            temp=[]
            cycle=n+1

            while cycle>0 and heap:
                cnt=heapq.heappop(heap)
                if cnt+1<0:
                    temp.append(cnt+1)
                time+=1
                cycle-=1

            for c in temp:
                heapq.heappush(heap,c)

            if heap:
                time+=cycle

        return time
