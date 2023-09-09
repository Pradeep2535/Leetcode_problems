
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p=1
        if len(s)!=len(t):p=0
        else:
            for i in s:
                if t.count(i)!=s.count(i):
                    p=0
        if p==0:return False
        else:return True
