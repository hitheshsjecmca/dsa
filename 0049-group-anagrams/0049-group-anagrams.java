class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> maps=new HashMap<>();

        for(String word:strs){
            char[] ch=word.toCharArray();
            Arrays.sort(ch);
            String key=new String(ch);
            if(!maps.containsKey(key)){
                maps.put(key,new ArrayList<>());
            }
            maps.get(key).add(word);
        }
        return new ArrayList<>(maps.values());
        
    }
}