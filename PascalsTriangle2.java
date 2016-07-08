import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

//https://leetcode.com/problems/pascals-triangle-ii/
public class PascalsTriangle2 {
	/**
	 * getRow 			Method gets the nth row of a Pascal Triangle and using O(k) extra spaces
	 * @param numRows   The nth row needed
	 * @return			Return the nth row of a Pascal Triangle
	 */
	public static List<Integer> getRow(int numRows) {
		 
		 List<Integer> level = new ArrayList<Integer>();
		 if(numRows == -1){
			 return level;
		 }
		 
		 if(numRows == 0){
			 level.add(1);
			 return level;
		 }
		
		 
		 List<Integer> trialLevel = new ArrayList<Integer>();
		 for(int j=1;j<=numRows;j++){
			 trialLevel.add(1);
			 for(int i=1;i<j;i++){
				 trialLevel.add(level.get(i-1)+level.get(i));
			 }
			 trialLevel.add(1);
			 Iterator<Integer> it = trialLevel.iterator();
			 level.clear();
			 while(it.hasNext()){
				 level.add(it.next());
			 }
			 
			 trialLevel.clear();
		 }
		 
		 return level;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(getRow(-1));
	}

}
