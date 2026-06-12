// public class DAY_8{
// class Solution {
//     public int[] getConcatenation(int[] nums) {
//         int n = nums.length;
//         int[] ans=new int[n*2];

//         for(int i=0;i<n;i++){
//         ans[i]=nums[i];
//         ans[i+n]=nums[i];
//         }
//         return ans;
//     }
// }
// }

// import java.util.HashSet;

// public class DAY_8{
//     class Solution {
//     public boolean hasDuplicate(int[] nums) {
//         HashSet<Integer> seen = new HashSet<>();

//         for(int i=0;i<nums.length;i++){
//             if(!seen.add(nums[i])){
//                 return true;
//             }
//         }
//         return false;
//     }
// }
// }

// import java.util.Arrays;

// public class DAY_8{
//     class Solution {
//     public boolean isAnagram(String s, String t) {
//         if(s.length()!=t.length())return false;

//         char[] sArr = s.toCharArray();
//         char[] tArr = t.toCharArray();

//         Arrays.sort(sArr);
//         Arrays.sort(tArr);

//         return Arrays.equals(sArr,tArr);
//     }
    
// }

// }