class Solution(object):
    def permute(self, nums):
        r=[]
        def bck(path):
            if len(path)==len(nums):
                r.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                bck(path)
                path.pop()
        
        bck([])
        return r
        