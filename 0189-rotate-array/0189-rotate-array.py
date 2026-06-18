class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)
        k%= n

        l, r=0, n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l,r=0, k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r=k, n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        '''self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1'''

        