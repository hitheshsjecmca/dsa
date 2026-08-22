class Solution {
    public int trap(int[] height) {
        int left=0;
        int right=height.length-1;
        int water=0;
        int bestleft=0;
        int bestright=0;

        while(left<right){
            if(height[left]<height[right]){
                if(height[left]>=bestleft){
                    bestleft=height[left];
                }else{
                    water+=bestleft-height[left];
                }
                left++;
            }else{
                if(height[right]>=bestright){
                    bestright=height[right];
                }else{
                    water+=bestright-height[right];
                }
                right--;
            }
        }
        return water;
    }
}