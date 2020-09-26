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
	 * 정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).
	 * 예제)
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
		System.out.print("정수를 입력해주세요.>>>");
		
	}

}
