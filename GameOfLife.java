// In-place solution
public class GameOfLife {
	/**
	 * gameOfLife Method gives an updated state of dead and live cells based on the rules 
	 * 			  defined in the question
	 * 
	 * @param board A 2d array with 1 as live cell and 0 as dead cell
	 */
	public void gameOfLife(int[][] board) {
		//Calculate all the live neighbors for each cell and also store each count with a flag.
		//Flag will depict whether the previous cell was alive or dead.
		//In my example I will use sign as a flag. If -ve: dead, +ve alive
		for(int i =0;i<board.length;i++){
			for(int j=0;j<board[0].length;j++){
				if(board[i][j]==0)
					board[i][j]= getNeighbors(board, i, j)*(-1);
				else
					board[i][j]= getNeighbors(board, i, j);
			}
		}
		//Lets call the rule book for each cell
		for(int i =0;i<board.length;i++){
			for(int j=0;j<board[0].length;j++){
				board[i][j]= ruleBook(board,i,j);
			}
		}
		//Print new state and verify
		for(int i =0;i<board.length;i++){
			for(int j=0;j<board[0].length;j++){
				System.out.print(board[i][j]);
			}
			System.out.println();
		}
    }
	/**
	 * ruleBook Method includes all the rules imposed to update the status of a cell
	 * @param board A 2d array with 1 as live cell and 0 as dead cell
	 * @param i Current row
	 * @param j Current column
	 * @return updated status - dead or alive
	 */
	public static int ruleBook(int[][] board, int i, int j){
		int cellValue=board[i][j];
		//If the cell was alive, there are 3 rules to follow
		if(cellValue>0)
		{
			if(cellValue<2)
				return 0;
			if(cellValue>=2&&cellValue<=3)
				return 1;
			if(cellValue>3)
				return 0;
		}
		//If dead and three neighbors
		if(cellValue==-3)
		{
			return 1;
		}
		return 0;
	}
	/**
	 * getNeighbours Method to get the number of neighbors alive
	 * @param board A 2d array with 1 as live cell and 0 as dead cell
	 * @param i Current row
	 * @param j Current column
	 * @return number of neighboring cells that are alive
	 */
	public static int getNeighbors(int [][]board, int i, int j){
		/*Since all the rules are dependent on how many neighbors are alive, we will count live 
		neighbors*/
		//Above
		int liveNeighbors = 0;
		if((i-1)>=0&&(j>=0)&&board[i-1][j]>0){
			liveNeighbors++;
		}
		//Left Side
		if(i>=0&&(j-1)>=0&&board[i][j-1]>0){
			liveNeighbors++;
		}
		
		//Above Diagonally left 
		if((i-1)>=0&&(j-1)>=0&&board[i-1][j-1]>0){
			liveNeighbors++;
		}
		//Below
		if(i+1<board.length&&j<board[0].length&&board[i+1][j]>0)
		{
			liveNeighbors++;
		}
		//Right Side
		if(i<board.length&&(j+1)<board[0].length&&board[i][j+1]>0)
		{
			liveNeighbors++;
		}
		//Above Diagonally Right
		if((i-1)>=0 && (j+1)<board[0].length&&board[i-1][j+1]>0){
			liveNeighbors++;
		}
		//Below Diagonally Left
		if(i+1<board.length && j-1>=0&&board[i+1][j-1]>0)
		{
			liveNeighbors++;
		}
		//Below Diagonally Right
		if(i+1<board.length && j+1<board[0].length&&board[i+1][j+1]>0)
		{
			liveNeighbors++;
		}
		//If all dead, then keep this cell alive
		if(liveNeighbors==0 && board[i][j]==1) 
			return 1;
		
		return liveNeighbors;
	}
	public static void main(String[] args) {
		
		int [][] board = new  int[][]{{1,0,1},{1,0,1},{0,0,1}};
		GameOfLife g = new GameOfLife();
		g.gameOfLife(board);

	}

}
