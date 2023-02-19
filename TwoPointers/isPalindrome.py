class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        for i in s:
            if ord('A') <= ord(i) <= ord('Z'):
                continue
            elif ord('a') <= ord(i) <= ord('z'):
                continue
            elif ord('0') <= ord(i) <= ord('9'):
                continue
            else:
                s = s.replace(i, "")
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
