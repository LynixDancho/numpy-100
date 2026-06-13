from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        max= float('inf')
        index = None
        for i in range(len(nums)):
            if target == nums[i]:
                return i 
            if target > nums[i]:

 
                    index = i +1
        if index :
            return index
        else : return 0 
        


            

        

 
yes = [1,3,5,6]
test = Solution.searchInsert(None,yes , 2 )

print(test)