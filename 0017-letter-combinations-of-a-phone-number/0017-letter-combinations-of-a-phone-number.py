from itertools import product

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        letters = [phone[d] for d in digits]

        ans = []
        for combo in product(*letters):
            ans.append("".join(combo))

        return ans