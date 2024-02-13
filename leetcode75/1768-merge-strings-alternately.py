

# Best Solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)


# My solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        x, y = 0, 0
        while x < len(word1) and y < len(word2):
            if x == y:
                merged += word1[x]
                x += 1
            else:
                merged += word2[y]
                y += 1
        merged += word1[x:]
        merged += word2[y:]
        return merged

sol = Solution()
w1 = "abcd"
w2 = "pq"
print(sol.mergeAlternately(w1, w2))

