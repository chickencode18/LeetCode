from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        phone = {
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs","8":"tuv","9":"wxyz"
        }

        def bt(index: int,path:str):
            if index == len(digits):
                res.append(path)
                return 
            
            let = phone[digits[index]]
            for letter in let:
                bt(index+1,path+letter)
        bt(0,"")
        return res