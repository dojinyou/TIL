package sort_algorithm;

import java.util.Arrays;

public class mergeSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public static int[] MergeSort(int[] arr) {
		// 고속 정렬 : O(nlogn)
        if (arr.length < 2) return arr;

        int mid = arr.length / 2;
        int[] low_arr = MergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] high_arr = MergeSort(Arrays.copyOfRange(arr, mid, arr.length));

        int[] mergedArr = new int[arr.length];
        int m = 0, l = 0, h = 0;
        while (l < low_arr.length && h < high_arr.length) {
            if (low_arr[l] < high_arr[h])
                mergedArr[m++] = low_arr[l++];
            else
                mergedArr[m++] = high_arr[h++];
        }
        while (l < low_arr.length) {
            mergedArr[m++] = low_arr[l++];
        }
        while (h < high_arr.length) {
            mergedArr[m++] = high_arr[h++];
        }
        // 중복 삭제 : O(n)
        int cnt = 0;
        int[] removedArr = new int[mergedArr.length];
        Arrays.fill(removedArr,mergedArr[0]);
        for (int i=0;i<mergedArr.length;i++) {
        	if (removedArr[cnt]!= mergedArr[i]) {
        		removedArr[++cnt] = mergedArr[i];
        	}
        }
        return Arrays.copyOfRange(removedArr, 0, cnt+1);
    }	

}
