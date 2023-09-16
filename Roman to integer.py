#Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        d={'C':100,'L':50,'M':1000,'D':500,'I':1,'V':5,'X':10}
        i=0
        res=0
        l=len(s)
        while(i<l):
            a=d[s[i]]
            if i+1<l:
                b=d[s[i+1]]
                if b>a:
                    res=res+b-a
                    i=i+2
                else:
                    i=i+1
                    res=res+a
            else:
                res=res+a
                i+=1
        return res
