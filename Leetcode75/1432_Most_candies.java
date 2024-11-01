import java.util.Collections; 
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = candies[0];
        for (int i = 0 ; i < candies.length ; i ++) {
            maxCandy = Math.max(maxCandy, candies[i]);
        }

        ArrayList<Boolean> answer = new ArrayList<>();
        for (int i = 0 ; i < candies.length ; i ++) {
            if (candies[i] + extraCandies >= maxCandy) {
                answer.add(true);
            } else {
                answer.add(false);
            }
        }
        return answer;
    }
}
