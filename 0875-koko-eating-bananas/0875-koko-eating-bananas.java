class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low=1;
        int hg = 0;

        for (int pile : piles) {
            hg = Math.max(hg, pile);
            }

        int ans=hg;

        while(low<=hg){
            int mid=(low+hg)/2;
            long hours=0;

            for(int pile:piles){
                hours+=(pile+mid-1)/mid;
                
            }
            if(hours<=h){
                ans=mid;
                hg=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
        
    }
}