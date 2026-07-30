class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):

                if i!=j :
                    product *= nums[j]

            answer.append(product)
        
        return answer
        