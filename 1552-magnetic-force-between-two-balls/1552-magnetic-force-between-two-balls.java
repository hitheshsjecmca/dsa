class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);

        int low=1;
        int high=position[position.length-1]-position[0];

        int ans=high;

        while(low<=high){
            int mid=low+(high-low)/2;

            int count=1;
            int lp=position[0];
            for(int i=0;i<position.length;i++){
                if(position[i]-lp>=mid){
                    count++;
                    lp=position[i];
                }
            }
            if(count>=m){
                ans=mid;
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return ans;
    }
}