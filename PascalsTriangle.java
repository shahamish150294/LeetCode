import java.util.ArrayList;
import java.util.List;

//https://leetcode.com/problems/pascals-triangle/
public class PascalsTriangle {
	/**
	 * generate Method is use to generate Pascal Triangle	 
	 * @param numRows Number of rows you want to enter
	 * @return List of list of that builds the triangle
	 */
	public static List<List<Integer>> generate(int numRows) {
			 
			 List<Integer> level = new ArrayList<Integer>();
			 List<List<Integer>> levels = new ArrayList<List<Integer>>();
			 
			 if(numRows == 0){
				 return levels;
			 }
			 level.add(1);
			 levels.add(level);
			 
			 if(numRows==1){
				 return levels;
			 }
			 
			 
			 
			 for(int j=1;j<numRows;j++){
		     List<Integer> level2 = new ArrayList<Integer>();
			 level2.add(1);
			 
				 for(int i=2;i<=j;i++){
					 level2.add(levels.get(j-1).get(i-2 ) + levels.get(j-1).get(i-1 ));
				 }
			 
			 level2.add(1);
			 levels.add(level2);
			 
			 }
			 
			 return levels;
		    }
	 public static void main(String args[]){
		 generate(1);
	 }
}
