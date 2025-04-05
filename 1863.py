class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxnum = max(nums)
        answer = 0
        power = 1
        while maxnum > 0:
            maxnum >>= 1
            count = 0
            for i in range(n):
                count += nums[i] % 2
                nums[i] >>= 1
            answer += power * (2**(n - 1) * (1 if count else 0))
            power <<= 1;
        return answer