class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # for i in range(len(height)):
        #     for j in range(i+1):
        #         h1 = height[i]
        #         idx1 = i
        #         h2 = height[j] 
        #         idx2 = j
        #         h = min(h1,h2)
        #         # print(idx1 - idx2)
        #         if max_area < abs(h*(idx1 - idx2)):
        #             max_area = abs(h*(idx1 - idx2))
        #             # print(max_area)
        # return max_area
    
        idx0, idx1, idx2 = 0, 0, len(height)-1
        while idx1 <= idx2:
            if abs(min(height[idx0],height[idx1])*(idx0 - idx1)) > max_area:
                max_area = abs(min(height[idx0], height[idx1])*(idx0 - idx1))
                idx1 += 1
                idx0 += 1
            elif abs(min(height[idx1],height[idx2])*(idx1 - idx2)) > max_area:
                max_area = abs(min(height[idx1], height[idx2])*(idx1 - idx2))
                idx1 += 1
                idx2 -= 1
            return max_area
            
