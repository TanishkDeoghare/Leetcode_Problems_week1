class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        # print(len(my_set))
        # print(len(nums))
        if len(my_set) == len(nums):
            return False
        else:
            return True
        