class Solution:
    def isValid(self, s: str) -> bool:
            diction  = {
                ']':'[',
                '}' :'{',
                ')' : '(',
            }
            stack = []
            if len(s) == 1:
                  return False
            for char in s:
                  
                  if char in diction and stack and    stack[-1] == diction.get(char) :
                       stack.pop()
                  else:
                        stack.append(char)
            if stack: return False
            else : return True

                  



 
my_string = "){"
result = Solution.isValid(None, s=my_string)  
print(result)

       
        