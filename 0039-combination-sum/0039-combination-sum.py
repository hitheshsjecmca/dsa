class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]

        def dfs(index,cur,total):
            if total==target:
                result.append(cur[:])
                return 
            
            if index >= len(candidates) or total>target:
                return 

            cur.append(candidates[index])
            dfs(index,cur,total+candidates[index])

            cur.pop()

            dfs(index+1,cur,total)
        dfs(0,[],0)    
        return result

        