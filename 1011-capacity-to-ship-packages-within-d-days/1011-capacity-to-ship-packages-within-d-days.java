class Solution {
    public int shipWithinDays(int[] weights, int days) {

        int low=0;
        int high=0;
        for(int weight:weights){
            low=Math.max(weight,low);
            high+=weight;
        }
        int ans=high;

        while(low<=high){
            int capacity=(low+high)/2;

            int curw=0;
            int rqd=1;
            for(int weight:weights){
                
                if(curw+weight>capacity){
                    rqd++;
                    curw=0;
                }
                curw+=weight;
            }
            if(rqd<=days){
                ans=capacity;
                high=capacity-1;
            }else{
                low=capacity+1;
            }

        }

        return ans;

        
    }
}