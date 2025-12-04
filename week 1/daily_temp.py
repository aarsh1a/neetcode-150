# push nis onto stack until higher encountered then pop until equal or lower
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        r=[0]*n
        numStack=[]
        for i,t in enumerate(temperatures):
            while numStack and t>temperatures[numStack[-1]]:
                prev=numStack.pop()
                r[prev]=i-prev
            numStack.append(i)

        return r