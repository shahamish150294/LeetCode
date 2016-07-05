//https://leetcode.com/problems/find-peak-element/
public class FindPeak {
	/**
	 * findPeakElement Method that calls findPeakUtil 
	 * @param nums     Pass integer array
	 * @return		   Index of the peak array
	 */
	public int findPeakElement(int[] nums) {
		/* Sol1: 
		 * int pre = Integer.MIN_VALUE, post = Integer.MIN_VALUE;
	    int numsSize = nums.length;
		for(int i = 0; i < numsSize; i++)
	    {
	        if(i == 0)
	            pre = Integer.MIN_VALUE;
	        else
	            pre = nums[i-1];
	        if(i == numsSize-1)
	            post = Integer.MIN_VALUE;
	        else
	            post = nums[i+1];
	        if(nums[i] > pre && nums[i] > post)
	            return i;
	    }*/
		
		
		return findPeakUtil(nums, 0, nums.length-1);
	}
	/**
	 * findPeakUtil Method finds the peak element position(i) where element at i-1 and i+1 are less than element at i
	 * @param nums 	   Integer array 
	 * @param low	   Start of sub array
	 * @param high	   End of sub array
	 * @return 		   Peak element position i
	 */
	 static int findPeakUtil(int arr[], int low, int high)
	    {
	        int mid = low + (high - low)/2; 

	        if ((mid == 0 || arr[mid-1] <= arr[mid]) && (mid == arr.length-1 ||
	             arr[mid+1] <= arr[mid]))
	            return mid;

	        else if (mid > 0 && arr[mid-1] > arr[mid])
	            return findPeakUtil(arr, low, (mid -1));

	        else return findPeakUtil(arr, (mid + 1), high);
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FindPeak f = new FindPeak();
							 
		int nums[]= new int[]{1,2,3,4};//{1,2,3,1};//{6,2,3,5,6}2;
		System.out.println(f.findPeakElement(nums));
	}

}
