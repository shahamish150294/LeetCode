import java.util.*;
class Solution2{
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
    	
    	//Map to store equation[0][0], equation[0][1]
    	HashMap<String, ArrayList<String>> equationMap = new HashMap<String,  ArrayList<String>>();
    	//Map to store equation and values
    	HashMap<String, ArrayList<Double>> eqValuesMap = new HashMap<String, ArrayList<Double>>();
    	
    	//Add equations to equationMap
    	for (int i=0;i<equations.length;i++){
    	    if (!equationMap.containsKey(equations[i][0])){
    	        equationMap.put(equations[i][0], new ArrayList<String>());
    	    }
    	    equationMap.get(equations[i][0]).add(equations[i][1]);
    	    if (!equationMap.containsKey(equations[i][1])){
    	        equationMap.put(equations[i][1], new ArrayList<String>());
    	    }
    	    equationMap.get(equations[i][1]).add(equations[i][0]);
    	}
    	
    	//Add equation and values to the other map
    	for (int i=0;i<equations.length;i++){
    	    if (!eqValuesMap.containsKey(equations[i][0])){
    	        eqValuesMap.put(equations[i][0], new ArrayList<Double>());
    	    }
    	    eqValuesMap.get(equations[i][0]).add(values[i]);
    	    if (!eqValuesMap.containsKey(equations[i][1])){
    	        eqValuesMap.put(equations[i][1], new ArrayList<Double>());
    	    }
    	    eqValuesMap.get(equations[i][1]).add(1/values[i]);
    	}
    	
    	double results[] = new double[queries.length];
    	HashSet<String> visited;
    	for (int i=0;i<queries.length;i++)
    	{
    	    visited = new HashSet<String>();
    	    results[i] = dfs(queries[i][0],queries[i][1], visited, equationMap, eqValuesMap, 1.0);
    	    if (results[i] == 0.0){
    	        results[i] = -1.0;
    	    }
    	    
    	}
    	
    	return results;
    }
    public static double dfs(String num, String den, HashSet<String> visited, HashMap<String, ArrayList<String>> equationMap, HashMap<String, ArrayList<Double>> eqValuesMap, double currentValue){
        if (visited.contains(num)) 
            return 0.0;
        
        if (!equationMap.containsKey(num))
            return 0.0;
            
        if (num.equals(den))
            return currentValue;
        //Mark the node visited
        visited.add(num);
        ArrayList<String> connectedNodes = equationMap.get(num);
        ArrayList<Double> connectedValues = eqValuesMap.get(num);
        double temp = 0.0;
        for (int i=0;i<connectedNodes.size();i++){
            temp =  dfs(connectedNodes.get(i), den, visited, equationMap, eqValuesMap, currentValue * connectedValues.get(i));
            if (temp!=0.0) break;
        }
        
        
        return temp;
    }


}
public class EvaluateDivision{
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
}
