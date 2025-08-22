class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sr=s.split()
        last=sr[-1]
        return len(last)
       


         
        