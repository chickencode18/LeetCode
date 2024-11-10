class Solution:
    def reverse(self, x: int) -> int:
        a = ""
        if x == 0: return x

        if x > 0:
            x = str(x)
            for i in x[::-1]:
                a += i
            x = int(a)
        else:
            x = str(-x)
            for i in x[::-1]:
                a += i
            x = -int(a)
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x