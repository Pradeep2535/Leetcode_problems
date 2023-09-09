class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=""
        y=min(strs,key=len)
        for i in range(0,len(y)):
            c=0
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    c=1
            if c==0:
                k+=strs[j][i]
            else:break
        return k 
