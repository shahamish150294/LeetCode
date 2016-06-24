//https://leetcode.com/problems/combination-sum/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombinationSum {
	/**
	 * combinationSum Method contains initializes listOfPaths and calls backtrack
	 * @param candidates integer array
	 * @param target Elements in the path must sum to target
	 * @return list of paths with each path summing to target
	 */
	 public List<List<Integer>> combinationSum(int[] candidates, int target) {
		 	Arrays.sort(candidates);
		    List<List<Integer>> listOfPaths = new ArrayList<>();
		    backTrack(candidates, target, 0, new ArrayList<>(), listOfPaths);
		    return listOfPaths;
	 }
	 /**
	  * backTrack Method is a simple backtracking approach like dfs
	  * @param candidates integer array
	  * @param target sum value which be reduced after every call
	  * @param i current element 
	  * @param path list of valid elements having sum greater than 0 and less than target
	  * @param listOfPaths if sum of elements in a path equals 0, add the path to this list
	  */
	 private void backTrack(int[] candidates, int target, int i, List<Integer> path, List<List<Integer>> listOfPaths){
		 if(target==0){
			 listOfPaths.add(path);
		 }
		 if(target<0){	
			 return;
		 }
		 /*Two imp things to note are the values of index j and passing the target's new value only as a parameter and not as by changing the 
		  * target's value in the for loop (like target = target - candidates[j])*/
		 for(int j=i;j<candidates.length;j++){
			 List<Integer> p = new ArrayList<>(path);
			 p.add(candidates[j]);
			 backTrack(candidates,target-candidates[j] , j, p,listOfPaths);
		 }
		 
	 }
	public static void main(String[] args) {
		CombinationSum c = new CombinationSum();
		int candidates[]= new int[]{2,3,6,7};
		int target = 7;
		System.out.println(c.combinationSum(candidates, target));
	}

}
