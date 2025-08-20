class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0

        
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substring = word[i:j]
                
                if set(substring).issubset(vowels):
                    
                  
                    if vowels.issubset(set(substring)):
                        count += 1

        return count