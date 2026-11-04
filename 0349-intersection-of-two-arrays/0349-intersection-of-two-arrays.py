class Solution(object):
    def intersection(self, nums1, nums2):
        hashmap={}
        for i in range(len(nums1)):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]]=i
        result=[]
        for i in range(len(nums2)):
            if nums2[i] in hashmap:
                if nums2[i] not in result:
                    result.append(nums2[i])
        return result
