class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                s = mul + ans[i + j + 1]

                ans[i + j + 1] = s % 10
                ans[i + j] += s // 10

        result = ""

        for x in ans:
            if result == "" and x == 0:
                continue
            result += str(x)

        return result