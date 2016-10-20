 class BalancedParantheses {
 
	static class Stack {
		char arr[] = new char[10];
		int size;
 
		void push(char a) {
			arr[size++] = a;
		}
 
		char pop() {
			if (size == 0)
				return ' ';
			return arr[--size];
 
		}
 
	}
 
	boolean isABalancedParantheses(String a) {
		boolean isBalanced = false;
		char ch[] = a.toCharArray();
		Stack st = new Stack();
		int popC = 0;
		int pushC = 0;
		for (int i = 0; i < ch.length; i++) {
			char c = ch[i];
			if (c == '[' || c == '{' || c == '(') {
				pushC++;
				st.push(c);
			}
			if (c == ']' || c == '}' || c == ')') {
				popC++;
 
				char pop = st.pop();
				if (c == ']' && pop == '[' || c == '}' && pop == '{' || c == ')' && pop == '(') {
					isBalanced = true;
				} else {
					isBalanced = false;
					break;
				}
 
			}
		}
		if (pushC != popC) {
			isBalanced = false;
		}
		return isBalanced;
	}
 
	public static void main(String a[]) {
		BalancedParantheses b = new BalancedParantheses();
		System.out.println(b.isABalancedParantheses("[()]{}{[()()]()}"));
		System.out.println(b.isABalancedParantheses("[][]][]"));
		System.out.println(b.isABalancedParantheses("[()}"));
 
	}
 
}