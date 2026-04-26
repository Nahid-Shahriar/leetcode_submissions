class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j= 0

        for i in range(len(nums)):
            if nums[i] != 0:
                
                nums[j], nums[i] = nums[i], nums[j]

                j += 1
    
        print(nums)

mysolution= Solution()
mysolution.moveZeroes([1,0,0,0,3,12])
                