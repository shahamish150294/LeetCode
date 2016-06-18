import java.util.Arrays;

public class MoveZeros {
	/**
	 * moveZeroes method moves all the numbers except zero to the left of the array and all the zeros to the right
	 * @param nums Integer array of numbers 
	 */
	public void moveZeroes(int[] nums) {
	    /*Use i to place numbers except 0 at proper places and when a 0 is encountered
	     * Start another pointer j to look for a number other than zero (l->r). 
	     * Swap that number with the number at i. Continue...
	     * */
		for(int i = 0;i<nums.length;i++){
			if(nums[i]==0){
			System.out.println("Position of 0: "+i);
				for(int j=i+1;j<nums.length;j++){
					
					if(nums[j]>0||nums[j]<0)
					{
						System.out.println("Position of num: "+j);
						int temp = nums[i];
						nums[i]=nums[j];
						nums[j]=temp;

						System.out.println("Array after swapping:");
						System.out.println(Arrays.toString(nums));	
						break;
					}
				}
				
			}
	    }
		
	    }
	public static void main(String arg[]){
		int[] nums= new int[]{1,3,4,5,6,7};
		MoveZeros a = new MoveZeros();
		a.moveZeroes(nums);
	}
}
