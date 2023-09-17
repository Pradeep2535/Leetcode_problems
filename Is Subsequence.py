'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a 
subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=len(t)
        k=0
        s1=""
        for i in range(l):
            
            if k<len(s) and t[i]==s[k]:
                s1+=t[i]
                k+=1
            if k>len(s):
                break
        if s=="":
            return True
        elif k==0 or s1!=s:
            return False
        else:
            return True
