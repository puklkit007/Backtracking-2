from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

      
        # 01 Recursion
        self.res = []
        
        def helper(index, path):
            if index == len(nums):
                self.res.append(path)
                return
            
            # Dont choose
            helper(index+1, path)
            # Choose
            helper(index+1, path + [nums[index]])
                        
        helper(0, [])
        return self.res
    
    
        # 01 recursion Backtracking
        self.res = []
        
        def helper(index, path):
            if index == len(nums):
                newPath = deepcopy(path)
                self.res.append(newPath)
                return
            
            # Dont choose
            helper(index + 1, path)
            # Action (because we need to insert the element first into the list before choosing it)
            path.append(nums[index])
            # Recurse
            # Choose
            helper(index + 1, path)
            # Backtrack
            path.pop()
                        
        helper(0, [])
        return self.res
        
        
        # For loop recursion
        self.res = []
        
        def helper(index, path):
            
            self.res.append(path)
            for i in range(index, len(nums)):
                newPath = path + [nums[i]]
                helper(i+1, newPath)
                    
        helper(0, [])
        return self.res
        
        
        # For Loop recursion Backtracking
        self.res = []
        
        def helper(index, path):
            
            newPath = deepcopy(path)
            self.res.append(newPath)
            for i in range(index, len(nums)):
                # Action
                path.append(nums[i])
                # Recurse
                helper(i+1, path)
                # Backtrack
                path.pop()

        helper(0, [])
        return self.res
        
        
        #Without Recursion
        res = [[]]

        for i in nums:
            size = len(res)
            for j in range(size):
                curr = res[j]
                newRes = deepcopy(curr)
                newRes.append(i)
                res.append(newRes)

        return res
