class Solution {
    public int splitArray(int[] nums, int k) {
        int left=0;
        int right=0;

        for(int num:nums){
            left=Math.max(left,num);
            right+=num;
        }
        int ans=right;

        while(left<=right){
            int maxsum=left+(right-left)/2;

            int part=1;
            int values=0;
            for(int num:nums){
                if(num+values>maxsum){
                    part++;
                    values=0;
                }
                values+=num;
            }
            if(part<=k){
                ans=maxsum;
                right=maxsum-1;
            }else{
                left=maxsum+1;
            }
        }
        return ans;
        
    }
}