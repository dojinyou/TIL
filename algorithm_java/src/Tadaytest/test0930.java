package Tadaytest;
import java.util.Scanner;

class Node{
	static final String[] items = {"(",")"};
	String item = "empty";
	Node left = null ; Node right = null;
	Node(){ }
	Node(int n){this.item = items[n];}
	Node(int n, Node left, Node right){
		this.item = items[n];
		this.left = left;
		this.right = right;
	}
}
public class test0930 {
	/*
	 * ���� n�� �־�����, n���� ���� ��ȣ "("�� n���� �ݴ� ��ȣ ")"�� ���� �� �ִ� ��ȣ ������ ��� ���Ͻÿ�. (�ð� ���⵵ ���� �����ϴ�).
	 * ����)
	 * Input: 1
	 * Output: ["()"]
	 * Input: 2
	 * Output: ["(())", "()()"]
	 * Input: 3
	 * Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
	 */
	
	public static String parathesisTree(int n){
		int cntLeft = n; int cntRight = n;
		String result = null;
		
		return result;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("������ �Է����ּ���.>>>");
		
	}

}
