package Tadaytest;
import java.util.Arrays;
import java.util.Vector;

public class intergerArrayTarget {
	public static void main(String[] args) {
		int[] testArray = {2,5,6,1,10};
		int target = 6;
//		Vector<Integer> upper = new Vector<Integer>();
//		Vector<Integer> lower = new Vector<Integer>();
//		for(int i = 0; i<testArray.length;i++) {
//			if(testArray[i]<target/2) {
//				int idx = target/2 - testArray[i];
//				lower.add(idx, i);
//				if(upper.get(idx)!=null) {
//					System.out.println("배열["+i+"] + 배열["+upper.get(idx)+"] = "+target);
//				}
//			} else {
//				int idx1 = testArray[i] - target/2; 
//				upper.add(idx1, i);
//				if(lower.get(idx1)!=null) {
//					System.out.println("배열["+i+"] + 배열["+upper.get(idx1)+"] = "+target);
//				}
//			}
//		}
		int[] upper = new int[testArray.length];
		int[] lower = new int[testArray.length];
		Arrays.fill(upper, -1); 
		Arrays.fill(lower, -1);
		for(int i = 0; i<testArray.length;i++) {
			if(testArray[i]<target/2) {
				int idx = target/2 - testArray[i];
				lower[idx] = i;
				if(upper[idx]!=-1) {
					System.out.println("배열["+upper[idx]+"] + 배열["+i+"] = "+target);
					break;
				}
			} else {
				int idx1 = testArray[i] - target/2; 
				upper[idx1] = i;
				if(lower[idx1]!=-1) {
					System.out.println("배열["+lower[idx1]+"] + 배열["+i+"] = "+target);
					break;
				}
			}
		}
			
	}
}
