class BSTNode {
		      int val;
		      BSTNode left;
		      BSTNode right;
		      BSTNode(int x) { val = x; }
	}
public class BSTRecover {
	
	public void recoverTree(BSTNode root) {
		BSTNode BSTarray[] = new BSTNode[3];
		BSTNode first = null;
		BSTNode second =null;
		BSTNode prev = null;
		BSTarray[0] = first;
		BSTarray[1] = second;
		BSTarray[2] = prev;
		recovery(root,BSTarray);
		int temp = BSTarray[0].val;
		BSTarray[0].val = BSTarray[1].val;
		BSTarray[1].val = temp;
		
    }
	public void recovery(BSTNode root, BSTNode[] BSTarray){
		
		if (root == null)
			return;
		recovery( root.left, BSTarray);
		if (BSTarray[2] != null){
			
		
		
			if (root.val < BSTarray[2].val){
				if (BSTarray[0] == null) BSTarray[0] = BSTarray[2];
				BSTarray[1] = root;
			}
		}
			BSTarray[2] = root;
		
		recovery( root.right, BSTarray);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BSTNode root = new BSTNode(0);
		root.left = new BSTNode(1);
//		root.left.left = new BSTNode(3);
//		root.left.right = new BSTNode(15);
//		root.right = new BSTNode(30);
//		root.right.left = new BSTNode(25);
//		root.right.right = new BSTNode(10);
		new BSTRecover().recoverTree(root);
		
	}

}
