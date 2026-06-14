memo= {}
def climbStairs( n: int) -> int:
    
        if n in memo:
             return memo[n]
        if n ==0 :
            return 1 
        if n <0:
            return 0
        a=  climbStairs(n=n-1) +climbStairs(n=n-2)
        memo[n] = a

            
        return a

        
        
test =climbStairs(5)
print(test)