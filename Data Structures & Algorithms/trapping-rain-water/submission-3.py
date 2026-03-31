class Solution:
    def trap(self, height: List[int]) -> int:
        Area = 0
        l,r = 0,len(height)-1
        leftMax = height[0]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                Area+=leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                Area += rightMax - height[r]
        return Area 
        
                    
                

            

            
            

        
        
            
        
        
            


        