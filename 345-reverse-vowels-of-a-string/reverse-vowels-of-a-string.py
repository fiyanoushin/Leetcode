class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        collected = ""
        for ch in s:
            if ch in vowels:
                collected += ch
        collected = collected[::-1]
        result = ""
        i = 0
        for ch in s:
            if ch in vowels:
                result += collected[i]
                i += 1
            else:
                result += ch
        return result
