class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = 0
        for x in nums:
            s += x
        
        if s % 2 != 0:
            return False
        
        target = s // 2
        maxnum = max(nums)
        if maxnum > target:
            return False
        if maxnum == target:
            return True

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for x in nums:
            if dp[target - x]:
                return True

            for y in range(target - x - 1, -1, -1):
                if dp[y]:
                    dp[y + x] = True

        return False