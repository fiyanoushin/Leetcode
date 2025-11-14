class Solution(object):
    def canConstruct(self,ransomNote, magazine):

        freq = {}

        for c in magazine:
            freq[c] = freq.get(c, 0) + 1

        for c in ransomNote:
            if c not in freq or freq[c] == 0:
                return False
            freq[c] -= 1

        return True


    
       
        