def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    mergeNums = []
    m = len(nums1)
    n = len(nums2)
    j = 0
    for i in range(0, m):
        while (j < n and nums1[i] >= nums2[j]):
            mergeNums.append(nums2[j])
            j = j + 1
        mergeNums.append(nums1[i])
    while (j < n):
        mergeNums.append(nums2[j])
        j = j + 1
    mid = (m + n - 1) % 2
    tmp = int((m + n - 1) / 2)
    if (mid == 0):
        median = float(mergeNums[tmp])
    else:
        median = (mergeNums[tmp] + mergeNums[tmp + 1]) / 2.0
    return median