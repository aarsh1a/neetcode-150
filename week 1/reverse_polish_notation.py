# normal stack postfix operation 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack=[]
        for i in tokens:
            if i not in "+-*/":
                numStack.append(int(i))
            else:
                b=numStack.pop()
                a=numStack.pop()
                if i=="+":
                    numStack.append(a+b)
                elif i=="-":
                    numStack.append(a-b)
                elif i=="*":
                    numStack.append(a*b)
                else:
                    numStack.append(int(a/b))
        return numStack[0]