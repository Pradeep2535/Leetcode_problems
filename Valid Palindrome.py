class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=s.replace(" ","")
        k=""
        for i in j:
            if i.isalnum():
                k+=i.lower()
        return k[::]==k[::-1]
