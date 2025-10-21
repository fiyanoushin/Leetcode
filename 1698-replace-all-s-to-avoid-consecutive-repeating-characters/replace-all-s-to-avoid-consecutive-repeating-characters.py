class Solution(object):
    def modifyString(self, s):
        s = list(s)  
        for i in range(len(s)):
            if s[i] == '?':
                prev = s[i - 1] if i > 0 else None
                nxt = s[i + 1] if i < len(s) - 1 else None
                for w in 'abc':
                    if w != prev and w != nxt:
                        s[i] = w
                        break
        return ''.join(s)

        