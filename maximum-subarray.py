# -*- coding:UTF-8 -*-
nums=input().split(',')
lens=len(nums)

#最简单的用循环处理问题，时间复杂度为O(n^2)，时间超出限制
def maxSum(lens,nums):
    maxSum=nums[0]    #存储最大和
    for i in range(lens):
        tmpSum=nums[i]   #计算每个子序的和
        for j in range(i+1,lens):
            if(tmpSum>maxSum):
                maxSum=tmpSum
            tmpSum=tmpSum+nums[j]
        if(tmpSum>maxSum):
            maxSum=tmpSum
    return maxSum

#接下来用动态规划的方法进行优化
def DP_maxSum(lens,nums):
    maxSum=nums[0]
    tmpSum=0
    for i in range(lens):
       tmpSum=tmpSum+nums[i]
       if(tmpSum>maxSum):
           maxSum=tmpSum
       if(tmpSum<0):
           tmpSum=0
