
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        freq = {}
        window = {}

        for x in p:
            freq[x] = freq.get(x, 0) + 1

        res = []
        k = len(p)

        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1

            if i >= k:
                left = s[i - k]
                window[left] -= 1

                if window[left] == 0:
                    del window[left]

            if window == freq:
                res.append(i - k + 1)

        return res
