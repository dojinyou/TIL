package sort_algorithm;

import java.util.Arrays;

public class CountingSort {

	public static void main(String[] args) {
        int[] a = {1,2,3,4,5,2,3,4,5,3,2,1,1,3,2,3,2,4,1,3};
        int result = CountingSort(a, 5, 1, 3);
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
        System.out.println(result);
	}
	public static int CountingSort(int[] array, int k, int a, int b) {
		// ��ó��
		int n = array.length;
		int[] cnt = new int[k+1];
		// count �ϴ� ���� : O(n)
		for (int i=0;i<n; i++) {
			cnt[array[i]] += 1;
		}
		// ���� ������Ű�� ���� : O(k)
		for (int i=1;i<k+1; i++) {
			cnt[i] += cnt[i-1];
		}
		// a~b ���� ���ҵ��� ���� ���� : O(1)
		return cnt[b] - cnt[a-1];
		
	}

}
