package sort_algorithm;

public class bubbleSort {
	public static void main(String[] args) {
//		int[] Array = {254,3,213,64,75,56,4,324,65,78,9,5,76,3410,8,342,76};
		int[] Array = {1,2,3,4,5,6,7};
		int temp;
		for(int i = 0 ; i < Array.length ; i ++) {
			// 변수 추가
			boolean swap = false;
			for(int j = 0 ; j < Array.length -i -1 ; j ++) {
				if(Array[j]>Array[j+1]) {
					temp = Array[j];
					Array[j] = Array[j+1];
					Array[j+1] = temp;
					swap = true;
				}
			}
			//조건문 추가
			if (!swap) {break;}
		}
	}
}
