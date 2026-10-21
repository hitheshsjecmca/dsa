class Solution(object):
    def checkInclusion(self, s1, s2):

        t=list(s1)
        t.sort()

        for i in range(len(s2)-len(s1)+1):
            cur=s2[i:i+len(s1)]
            cur_list=list(cur)
            cur_list.sort()

            if cur_list==t:
                return True

        return False