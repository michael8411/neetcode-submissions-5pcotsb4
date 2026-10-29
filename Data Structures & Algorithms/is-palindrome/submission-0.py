class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if  (ord('a') <= ord(c) <= ord('z')) or ord('A') <= ord(c) <= ord('Z') or (ord('0') <= ord(c) <= ord('9')):
                string += c 
        return string.lower() == string.lower()[::-1]    