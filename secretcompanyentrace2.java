import java.util.Arrays;
import java.util.Comparator;

public class secretcompanyentrace2 {

        public static void main(String[] args){

        Integer[] nums = {}; int l, r;
        nums = sort(nums);

        int max_l = -1; int min = l;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] > min){
                if(nums[i] < r) {
                    if (nums[i] - min > max_l) {
                        max_l = nums[i] - min;
                        
                    }
                    min = nums[i] + 1;
                }else{
                    if(nums[i] == r){
                        if (r - min > max_l) {
                            max_l = r - min;
                            min = nums[i] + 1;
                        }
                    }else{
                        break;
                    }

                }
            }
        }

        System.out.println(max_l);
    }

    static Integer[] sort(Integer[] arr){
        Arrays.sort(arr, new Comparator<Integer>()
        {
            @Override
            public int compare(Integer x, Integer y){
                return x-y;
            }
        });

        return arr;
    }

}
