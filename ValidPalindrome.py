class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        edit_s = ''.join(ltr.lower() for ltr in s if ltr.isalnum())
        
        for i in range(len(edit_s)//2):
            if edit_s[i] != edit_s[-(i+1)]:
                return False
        
        return True
