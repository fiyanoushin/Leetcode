class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        clean = ""
        for ch in paragraph.lower():
            if ch.isalpha():
                clean += ch
            else:
                clean += " "  
        words = clean.split()
        freq = {}
        banned_set = set(banned)
        
        for w in words:
            if w not in banned_set:
                freq[w] = freq.get(w, 0) + 1
        return max(freq, key=freq.get)
       