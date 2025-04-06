class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        val = [1 for _ in range(n)]
        pre = [-1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j] == 0) and (val[i] < val[j] + 1):
                    val[i] = val[j] + 1
                    pre[i] = j
        maxval = max(val)
        i = val.index(maxval)
        ans = []
        while (i != -1):
            ans.append(nums[i])
            i = pre[i]

        return ans
        
                    
