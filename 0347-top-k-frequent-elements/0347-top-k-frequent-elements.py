class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}

        # Count frequency
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # Sort based on frequency
        sorted_items = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)

        # Get top k elements
        return sorted_items[:k]