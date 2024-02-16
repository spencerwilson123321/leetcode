
# Best solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        # If the strings are equal to each other when concatenated, then we know that there exists a gcd.
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]


# My solution
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = ""
        str1 = str1.upper().strip()
        str2 = str2.upper().strip()
        smallest = str1 if len(str1) <= len(str2) else str2
        largest = str2 if len(str2) >= len(str1) else str1
        substrings = [smallest[:i+1] for i in range(0, len(smallest))]
        for sub in substrings:
            if largest.replace(sub, "") == "" and smallest.replace(sub, "") == "":
                gcd = sub
        return gcd


s1 = "ABCABC"
s2 = "ABC"
sol = Solution()
print(sol.gcdOfStrings(s1, s2))

