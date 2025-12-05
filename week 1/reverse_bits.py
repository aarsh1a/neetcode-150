class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            lastBit=n&1
            result=(result << 1) | lastBit
            n>>=1
        return result
