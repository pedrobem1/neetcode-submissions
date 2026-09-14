class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
         
        memo = {0:0}
        coins.sort()

        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            
            minn = float('inf')
            for coin in coins:
                diff = amt - coin

                if diff < 0:
                    break

                minn = min(minn, 1 + min_coins(diff))

            memo[amt] = minn
            return minn
        
        result = min_coins(amount)

        if result < float('inf'):
            return result
        else:
            return -1