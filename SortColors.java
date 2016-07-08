import java.util.Arrays;

//https://leetcode.com/problems/sort-colors/	
public class SortColors {
	/**
	 * sortColors	Method uses 3 way partitioning to sort numbers 0,1,2 occurences in the array
	 * @param nums	Integer array containing only 0s,1s and 2s
	 */
public static void sortColors(int[] nums) {
    int mid = 0;
    int low = 0;
    int high = nums.length-1;
    int temp;
    
    while(mid<=high){
    	switch (nums[mid]){
    	
    	case 0:
    		swap(low, mid, nums);
    		mid++;low++;
    	break;
    	
    	case 1:
    		mid++;
    	break;
    	
    	case 2:
    		swap(high, mid, nums);
    		high--;
    	break;
    	
    	}
    	
    }
    System.out.println(Arrays.toString(nums));
    }
	/**
	 * swap		Method to swap numbers
	 * @param a Index 1 for swapping
	 * @param b Index 2 for swapping
	 * @param nums Array in which swapping is to be done
	 */
	public static void swap(int a, int b, int[] nums){
		int temp = nums[a];
		nums[a] = nums[b];
		nums[b] = temp;
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int nums[]= new int[]{0,1,2,0,0};
		sortColors(nums);
	}

}
