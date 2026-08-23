class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first=lb(nums,target);
        int last=ub(nums,target)-1;

        if(first==nums.length || nums[first]!=target){
            return new int[]{-1,-1};
        }
        return new int[]{first,last};
        
    }
    public int lb(int[] nums,int target){
        int low=0;
        int high=nums.length-1;

        int ans=nums.length;;
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]>=target){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;

    }
    public int ub(int[] nums,int target){
        int low=0;
        int high=nums.length-1;
        int ans=nums.length;
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]>target){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
    }
}