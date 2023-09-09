class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=""
        y=min(strs,key=len)
        for i in range(0,len(y)):
            p=strs[0][i]
            c=0
            for j in range(len(strs)):
                if p!=strs[j][i]:
                    c=1
            if c==0:
                k+=strs[j][i]
            else:break
        return k 
