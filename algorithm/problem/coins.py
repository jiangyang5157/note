# Input: coins, amount
# Output: minimum number of needed coins for reaching the amount

from typing import List
    
class Solution:
    
    def main(self, coins: List[int], amount: int) -> int:
        if amount < 0: 
            return -1

        if amount == 0: 
            return 0
       
        coins.sort()

        if amount < coins[0]: 
            return -1
        
        if amount in coins: 
            return 1
        
        flag = [[False] * (amount + 1) for _ in range(amount + 1)]
        for coin in coins:
            if amount > coin:
                flag[0][coin] = True  

        for i in range(1, amount + 1):
            for j in range(1, amount + 1):
                if flag[i-1][j]:
                    for coin in coins:
                        if j + coin == amount:
                            return i + 1
                        if j + coin < amount:
                            flag[i][j+coin] = True
                            
        return -1
                    
print(Solution().main([1, 4, 2, 3, 5], 0)) # 0
print(Solution().main([1, 4, 2, 3, 5], 5)) # 1
print(Solution().main([1, 4, 2, 3, 5], 7)) # 2
