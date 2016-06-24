//https://leetcode.com/problems/majority-element/
public class MajorityElement {
	/**
	 * majorityElement Method to find element greater than Ln/2_|
	 * @params	integer array
	 * 
	 */
	public int majorityElement(int[] nums) {
        /*The n/2 is the main hint to solve this problem optimally. Store current element in a temp variable. Init the count variable to 1.
         * Go to the next element. If it is as temp, then increase the count else decrease. traverse the whole array. But while traversing if the 
         * count becomes 0 then the current element becomes temp and count is increased by one. This makes sure if  the count of 
         * temp reaches 0, then assign current as new temp. And it will never happen that temp will not be majority element*/
		int count = 1;
		int majorityElement = nums[0];
		for(int i =1; i<nums.length;i++)
		{
			if(nums[i]==majorityElement)
				count++;
			else
				if(count==0){
					majorityElement=nums[i];
					count++;
				}
				else{
					count--;
				}
		}
		
		return majorityElement;
    }
	
	
	
	public static void main(String args[]){
		MajorityElement m = new MajorityElement();
		int []nums = new int[]{1,2,3,4,5,6,1,1,1,1};
		System.out.println(m.majorityElement(nums));
	}
}
