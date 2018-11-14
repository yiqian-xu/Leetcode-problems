class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # using dynamic programing to solve the problme
        
        self.MOD = 10**9+7
        #p is represents the dialing pad 
        self.p = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','*']]
        
        # the dp array is 4*3 represents the amount of the dialed numbers when ending one a certain key
        dp = [[1]*3 for _ in xrange(4)]
        dp[3][0]=0 # the two keys on the left and right of '0' will never get pressed. 
        dp[3][2]=0
        dirs =[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        # looping through N-1 dials, cause number keys in the dp array are initialized with 1 as the first press
        for _ in xrange(1,N):
            
            n1 = dp[1][2]+dp[2][1]
            n2 = dp[2][0]+dp[2][2]   
            n3 = dp[1][0]+dp[2][1]
            n4 = dp[0][2]+dp[2][2]+dp[3][1]
            n5 = 0
            n6 = dp[0][0]+dp[2][0]+dp[3][1]
            n7 = dp[0][1]+dp[1][2]
            n8 = dp[0][0]+dp[0][2]
            n9 = dp[1][0]+dp[0][1]
            n0 = dp[1][0]+dp[1][2]
            dp[0][0]=n1%self.MOD
            dp[0][1]=n2%self.MOD
            dp[0][2]=n3%self.MOD
            dp[1][0]=n4%self.MOD
            dp[1][1]=n5%self.MOD
            dp[1][2]=n6%self.MOD
            dp[2][0]=n7%self.MOD
            dp[2][1]=n8%self.MOD
            dp[2][2]=n9%self.MOD
            dp[3][1]=n0%self.MOD
        return sum([sum(l) for l in dp])%self.MOD
