class Node{
	Node left;
	Node right;
	int data;
	Node(int data){
		this.data = data;
	}
}
public class BtreeInorderSuccessor {
	/**
	 * Traverse BST
	 * @param root
	 * @return The address of the node that whose next we 
	 * are looking for
	 */
	public static Node searchNode(Node root, int data){
		while (root != null)
		if(root.data >= data)
			root = root.left;
		else{
			root= root.right;
		}
		return root;
	}
	/**
	 * This method does not use parent pointer. It takes the 
	 * advantage that if root(the node that holds the data whose 
	 * next we are looking for) does not have a right child. Then its 
	 * next will be that 'x' node whose that has a left child who is the 
	 * parent of our root. So we keep track of that 'x' node
	 * @param root
	 */
	public static int nextSuccessor(Node root, int data){
		
		Node target = searchNode(root, data);
		if (root == null || target == null){
			return -1;
		}
		//Check if the node has right child
		if (target.right != null){
			return target.right.data;
		}
		Node x = null;
		while (root != null){
			if (root.data >= data){
				x = root;
				root = root.left;
			}
			else if (root.data > data){
				root = root.right;
			}
			else{
				break;
		
		
			}
		}
		return x.data;
	}
	public static void main (String arg[]){
		
	}
}
