from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        if digits[0] != 9:
            digits[0]=digits[0]+1
            return digits[::-1]
        for i in range(len(digits)):
            
            if digits[i] !=9:    
                print(digits[i])
                digits[i] = digits[i] +1
                return digits[::-1]
            digits[i] =0
            
        digits.append(1)
        return digits[::-1]






yes = Solution.plusOne(None,[8,9,9,9])




print( yes)