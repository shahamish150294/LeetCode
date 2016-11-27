package LetterCombinatioPhNo;
import java.util.*;
public class Solution {
    static HashMap<Integer,String> mapNumbers;
    public static void initializeMap(){
        mapNumbers= new HashMap<Integer,String>();
        mapNumbers.put(2,"abc");
        mapNumbers.put(3,"def");
        mapNumbers.put(4,"ghi");
        mapNumbers.put(5,"jkl");
        mapNumbers.put(6,"mno");
        mapNumbers.put(7,"pqrs");
        mapNumbers.put(8,"tuv");
        mapNumbers.put(9,"wxyz");
    }
    public static List<String> letterCombinations(String digits) {
        initializeMap();
        
        
        int indexDigit = 0;
        List<String> tempResults1 = new ArrayList<String>();  
        List<String> tempResults2 = new ArrayList<String>();;
        while(indexDigit<digits.length()){
        	String currentLetters = mapNumbers.get((int)digits.charAt(indexDigit)-48);
        	if (currentLetters == null){
        		indexDigit++;
        		continue;
        	}
            tempResults2 = new ArrayList<String>();      
            if (indexDigit ==0){
                
                
                tempResults1 = addToList(currentLetters, tempResults1);
                tempResults2 = tempResults1;
            }
            else{
            	
                
                for (String s: tempResults1){
                    for (int i=0;i<currentLetters.length();i++){
                        tempResults2.add(s+String.valueOf(currentLetters.charAt(i)));
                    }
                }
                
                tempResults1 = tempResults2;
            }
            indexDigit++;
        }
        return tempResults2;
    }
    public static List<String> addToList(String s, List<String> results){
        for(int i=0;i<s.length();i++){
            results.add(String.valueOf(s.charAt(i)));
        }
        return results;
    }
    public static void main(String args[]){
    	
    	String digits = new String ("2");
    	System.out.println((letterCombinations(digits)));
    	
    }
}