
# Best solution


# My solution
#class Solution(object):
#    def gcdOfStrings(self, str1, str2):
#        """
#        :type str1: str
#        :type str2: str
#        :rtype: str
#        """
#        str1 = str1.upper().strip()
#        str2 = str2.upper().strip()
#        smallest = str1 if len(str1) <= len(str2) else str2
#        largest = str2 if len(str2) >= len(str1) else str1
#        gcd = ""
#        for i in range(len(smallest)+1):
#            sub = smallest[0:i]
#            if sub in largest:
#                gcd = sub
#        return gcd
#

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
        for i in range(len(smallest)+1):
            sub = smallest[0:i]
            if largest.replace(sub,"") == "" and sub.replace(gcd, ""):
                gcd = sub
        return gcd


s1 = "ABABABAB"
s2 = "ABAB"
sol = Solution()
print(sol.gcdOfStrings(s1, s2))

