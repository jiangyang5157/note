# Input: List of integes, target
# Output: find 3 interges from the List which sum is the most closest to the target

from typing import List

class Solution:

    def main(self, nums: List[int], target: int) -> int:
        result = float('inf')
        min_test = float('inf')
        
        n=len(nums)
        nums.sort()

        for i in range(n):
            L=i+1
            R=n-1
            
            while(L<R):
                print(nums[i]+nums[L]+nums[R])
                if abs(nums[i]+nums[L]+nums[R]-target) < min_test:
                        result = nums[i]+nums[L]+nums[R]
                        min_test = abs(nums[i]+nums[L]+nums[R]-target)
                        
                if(nums[i]+nums[L]+nums[R]==target):
                    result = target
                    return result
                elif(nums[i]+nums[L]+nums[R] > target):
                    R=R-1
                else:
                    L=L+1
                    
        return result
    
print(Solution().main([1,2,4,8,16,32,64,128], 82))
