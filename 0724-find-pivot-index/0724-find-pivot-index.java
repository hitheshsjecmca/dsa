class Solution {
    public int pivotIndex(int[] nums) {

        int totalsums=0;
        for(int x:nums){
            totalsums+=x;
        }

        int left=0;
        int pivot=-1;

        for(int i=0;i<nums.length;i++){
            int right=totalsums-left-nums[i];

            if(left==right){
                pivot=i;
                break;
            }
            left+=nums[i];
        }
        return pivot;
        
    }
}