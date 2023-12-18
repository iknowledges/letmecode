#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return 1
        slow = fast = 1
        while fast < size:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

