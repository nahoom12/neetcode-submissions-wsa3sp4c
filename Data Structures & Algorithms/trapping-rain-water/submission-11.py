class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = [0] * n
        leftMax = [0] * n
        Water = 0
        #create a leftMax Array
        leftMax[0] = height[0] 
        for i in range(1,n):
            leftMax[i] = max(leftMax[i - 1],height[i])
        #create a rightmax value
        rightMax[n-1] = height[n-1]
        for i in range( n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        for i in range(n):
            Water += min(leftMax[i],rightMax[i])- height[i]
        return Water


        
                    
                

            

            
            

        
        
            
        
        
            


        