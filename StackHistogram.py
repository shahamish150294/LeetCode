class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        i = 0
        n = len(heights)
        stack =[]
        max_area = 0
        while i<n:
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i +=1

            else:
                top = stack.pop()

                if len(stack) > 0:
                    current_area = heights[top] * (i - stack[-1] - 1)
                else:
                    current_area = heights[top] * i

                if max_area < current_area:
                    max_area = current_area
        while len(stack) > 0:
            top = stack.pop()

            if len(stack) > 0:
                current_area = heights[top] * (i - stack[-1] - 1 )
            else:
                current_area = heights[top] * i
            if max_area < current_area:
                 max_area = current_area
        return max_area
print Solution().largestRectangleArea([4,2,0,3,2,5])