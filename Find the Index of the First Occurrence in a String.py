class Solution:
    def strStr(self, h: str, needle: str) -> int:
       
        if h.count(needle)==0:
            return -1
        d=0
        for i in range(0,len(h)):
            for j in range(i+1,len(h)+1):
                p=h.count(needle,i,j)
        
                if p==1:
                    if len(h[i:j])==len(needle):
                        
                        return i
        return 0          
            
