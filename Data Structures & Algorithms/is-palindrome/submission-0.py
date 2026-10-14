class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        mid = len(s) // 2
        a = s[:mid]
        b = s[mid + len(s) % 2:]
        c = b[::-1]

        if a == c:
            return True
        return False