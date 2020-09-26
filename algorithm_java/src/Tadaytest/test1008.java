package Tadaytest;
/* 
 * 정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 
 * 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 
 * 단, 정수를 문자열로 바꾸면 안됩니다.
 */

import java.util.Scanner;

public class test1008 {
	public static String check(int n) {
		int longOfInt = 1;
		int div = 10;
		while (n/div != 0) { //정수의 길이 확인
			longOfInt += 1;
			div *= 10;
		}
		int[] intArray = new int[longOfInt];
		int integer = n;
		for(int i = 0; i<intArray.length;i++) {
			System.out.println("integer = "+integer);
			intArray[i] = integer%10;
			integer = integer/10;
			System.out.println(i+"번째 정수는 "+intArray[i]);
		}
		for(int i=0; i<(longOfInt/2);i++) {
			if(intArray[i]!=intArray[longOfInt-i-1]) {
				return "palindrome이 아닙니다";
			}
		} return "palindrome입니다.";
	}
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("정수를 입력해주세요>>>");
		int n = scanner.nextInt();
		System.out.println(test1008.check(n));
	}
}
