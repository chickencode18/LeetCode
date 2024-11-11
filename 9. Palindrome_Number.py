class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0): return False
        a = str(x)
        return x == int(a[::-1])