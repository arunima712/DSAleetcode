class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans=[1]*n
        pre_product=1
        for i in range(0,n):
            ans[i] = pre_product
            pre_product= pre_product*nums[i]
        post_product=1
        for i in range(n-1,-1, -1):
            ans[i]=ans[i]* post_product
            post_product=post_product*nums[i]
        return ans            