class Solution(object):
    def increasingTriplet(self, nums):
        fr=float('inf')
        ls=float('inf')

        for x in nums:
            if x<=fr:
                fr=x
            elif x<=ls:
                ls=x
            else:
                return True

        return False
        