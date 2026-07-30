class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_items = sorted(count.items() , key = lambda x : x[1] , reverse = True)
        top_k = sorted_items[:k]
        result = [pair[0] for pair in top_k]
        return result