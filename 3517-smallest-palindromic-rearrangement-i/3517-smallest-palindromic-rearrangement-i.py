class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        # Count frequency
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        # Build left half
        for i in range(26):
            left.append(chr(i + ord('a')) * (freq[i] // 2))

            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

        left = "".join(left)

        # Right half
        right = left[::-1]

        return left + middle + right