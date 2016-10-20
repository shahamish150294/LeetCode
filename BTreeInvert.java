class TreeNode {
		      int val;
		      TreeNode left;
		      TreeNode right;
		      TreeNode(int x) { val = x; }
	}
public class BTreeInvert {
	
	public TreeNode invertTree(TreeNode root){
		if (root == null)
			return null;
		
			
		TreeNode left = invertTree(root.left);
		TreeNode right = invertTree(root.right);
		TreeNode temp;
		temp = left;
		root.left = right;
		root.right = temp;
		
		return root;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(4);
		//root.left = new TreeNode(2);
		//root.left.left = new TreeNode(1);
		//root.left.right = new TreeNode(3);
		root.right = new TreeNode(7);
		//root.right.left = new TreeNode(6);
		//root.right.right = new TreeNode(9);
		
		TreeNode a = (new BTreeInvert().invertTree(root));
		System.out.println(a);
	}

}
