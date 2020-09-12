import java.util.Scanner;

public class test {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
	    System.out.print("연산식 >> "); 
			double a = scanner.nextDouble();
	    Char operator = scanner.next();
			double b = scanner.nextDouble();
			
			System.out.println("a = "+a);
			System.out.println("b = "+b);
			System.out.println("op = "+operator);
	    switch (operator){
				case "+" {}
			}
	    	System.out.println(a + operator + b + "의 계산 결과는 " + (a+b) );
	    } else if (operator == "-") {
	    	System.out.println(a + operator + b + "의 계산 결과는 " + (a-b));
	    } else if (operator == "*") {
	    	System.out.println(a + operator + b + "의 계산 결과는 " + (a*b) );
	    } else if (operator == "/") {
	         if (b == 0) {
	            System.out.println("0으로 나눌 수 없습니다.");
	         } else {
	            System.out.println(a + operator + b + "의 계산 결과는 " + (a/b) );
	         }
        } else if (operator == "%") {
	         if (b == 0) {
	            System.out.println("0으로 나눌 수 없습니다.");
	         } else {
	            System.out.println(a + operator + b + "의 계산 결과는 " + (a%b) );
	         }
	    } else {
	         System.out.println("else 출력");
	    }
	    scanner.close();

	}

}