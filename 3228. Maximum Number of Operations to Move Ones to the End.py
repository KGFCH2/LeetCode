class Solution:
    def maxOperations(self, s: str) -> int:

        zero_segments=0
        res=0
        for i in reversed(range(len(s))):
            if s[i]=="0":
                if(i==len(s)-1 or s[i+1]=="1"):
                    zero_segments+=1
            else:
                res+=zero_segments
        return res        