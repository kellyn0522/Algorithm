# 해시 방식 사용
# 시간 복잡도 : O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target-num], i]
            num_map[num] = i
