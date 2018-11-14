class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        from math import sqrt
        #put all the squares of numbers what are smaller than n into an array called coins (like the coin change problem :D)
        coins = [i**2 for i in range(1,int(sqrt(n))+1)]
        #create the dp array of length n+1 represents the current least number of perfect squares of every nonnegative number <=n, initialzed with inf. 
        dp = [float('inf')]*(n+1)
        #since 0**2 doesn't count towards the number of perfect squares, so dp[0] is 0
        dp[0]=0 
        
        #for every c in coins check loop over every number i <=n, the number of perfect squares of i will be dp[i-c]+1.
        #since the least is the goal, we will compare the current dp[i] and the dp[i-c]+1 and take the smaller one as the new dp[i] 
        for c in coins:
            for i in xrange(1,n+1):
                if i>=c:
                    dp[i]=min(dp[i],dp[i-c]+1)
        
        
        return dp[n]
