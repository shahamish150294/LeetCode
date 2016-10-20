
public class isSubsequence {
	
	    public static boolean isSubsequence(String s, String t) {
	        
	        int j =0 ;
	        int m = s.length();
	        if (m==0){
	            return true;
	        }
	        
	        int n = t.length();
	        if (m>n) return false;
	        for(int i=0;i<n; i++){
	            if (j<m&&s.charAt(j)==
	            t.charAt(i)){
	                j++;
	            }
	        }
	        if (j == m){
	            return true;
	        }
	        return false;
	    }
	public static void main(String arg[]){
		System.out.println(isSubsequence("abc","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"));
	}
}
