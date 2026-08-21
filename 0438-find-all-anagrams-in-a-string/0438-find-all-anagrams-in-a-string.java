class Solution {
    public List<Integer> findAnagrams(String s, String p) {
       List<Integer> result = new ArrayList<>();
     char[] target=p.toCharArray();
     Arrays.sort(target);

     for(int i=0;i<=s.length()-p.length();i++){
        String cur=s.substring(i,i+p.length());

        char[] le=cur.toCharArray();

        Arrays.sort(le);
        if(Arrays.equals(le,target)){
            result.add(i);
        }
     }   
     return result;
    }
}