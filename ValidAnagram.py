class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        if length != len(t):
            return False
        
        counts = [0]*26
        for i in range(length):
            counts[ord(s[i])-97] -= 1
            counts[ord(t[i])-97] += 1
        
        for val in counts:
            if val != 0:
                return False
            
        return True
