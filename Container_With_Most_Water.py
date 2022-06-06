class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        Brute Force
        maxarea = 0
        for left in range(len(height)):
            for right in range(left+1, len(height)):
                width = right -left
                maxarea = max(maxarea, min(height[left], height[right]) * width) 
        
        return maxarea
        Time = O(n^2)"""
        """Two pointer approach"""
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right -left
            maxarea = max(maxarea, min(height[left] , height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea    

myobj = Solution()
height = [1,8,6,2,5,4,8,3,7]
maxarea = myobj.maxArea(height)
print(maxarea)