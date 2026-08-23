class Solution {
    public int shipWithinDays(int[] weights, int days) {

        int low=0;
        int high=0;

        for(int weight:weights){
            low=Math.max(low,weight);
            high+=weight;
        }
        int ans=high;

        while(low<=high){
            int capacity=low+(high-low)/2;
            int cw=0;
            int cd=1;
            for(int weight:weights){
               

                if(cw+weight>capacity){
                    cd++;
                    cw=0;
                }
                cw+=weight;
            }
            if(cd<=days){
                ans=capacity;
                high=capacity-1;
            }else{
                low=capacity+1;
            }
        }
        return ans;

        
    }
}