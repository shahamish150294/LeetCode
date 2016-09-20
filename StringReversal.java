
public class StringReversal {
	// recursive solution
	public static String recursiveReversal(String input, int end) {
		String x = "";
		if (end == -1) {
			return "";
		} else {
			x = recursiveReversal(input, end - 1);
			x = input.substring(end, end + 1) + x;
		}

		return x;
	}

	// By using charArray
	public static String reverseString(String input) {
		char[] temparray = input.toCharArray();
		int left, right = 0;
		right = temparray.length - 1;
		for (left = 0; left < right; left++, right--) {
			// Swap values of left and right
			char temp = temparray[left];
			temparray[left] = temparray[right];
			temparray[right] = temp;
		}
		input = "";
		for (char c : temparray)
			input += String.valueOf(c);
		return input;
	}

	// Using byteArray
	public static String reverseString2(String input) {
		byte[] strAsByteArray = input.getBytes();
		byte[] result = new byte[strAsByteArray.length];

		for (int i = 0; i < strAsByteArray.length; i++) {
			result[i] = strAsByteArray[strAsByteArray.length - i - 1];
		}
		return (new String(result));
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
