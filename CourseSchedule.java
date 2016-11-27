import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

public class CourseSchedule {
	public static void main(String arg[]){
		int [][]prerequisites = new int[][]{{1,0},{0,1}};
		
		int numCourses = 2;
//		if (new Solution().canFinish(numCourses, prerequisites)) System.out.println("possible"); else System.out.println("impossible");
		boolean sol = (new Solution().canFinish(numCourses, prerequisites));
	System.out.println(sol);
		/*for (int i=0;i<sol.length;i++){
			System.out.println(sol[i]);
		}*/
	}
}

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        boolean[] used = new boolean[numCourses];
        Neighbors[] graph = new Neighbors[numCourses];

        for (int i = 0; i < graph.length; i++) {
            graph[i] = new Neighbors();
        }

        for (int[] tuple : prerequisites) {
            graph[tuple[1]].neighbor.add(tuple[0]);
        }
        //To check for a cycle, use the boolean array below. If an index is true, that means that the node
        //is currently inside the stack. Once, you visited all the children of this node set the respective index to false
        boolean[] dfs = new boolean[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (topSort(i, graph, used, dfs)) {
                return false;
            }
        }

        return true;
    }

    class Neighbors {
        List<Integer> neighbor = new ArrayList<>();
    }

    private boolean topSort(int course, Neighbors[] graph, boolean[] used, boolean[] dfs) {
        if (used[course]) {
            return false;
        }
        //Check for cycle
        if (dfs[course]) {
            return true;
        }
        dfs[course] = true;
        for (int adj : graph[course].neighbor) {
            if (topSort(adj, graph, used, dfs)) {
            	//Cycle present
                return true;
            }
        }
        //No children left to visit, so set the respective index in dfs to false
        dfs[course] = false;
        
        used[course] = true;
        return false;
    }
}