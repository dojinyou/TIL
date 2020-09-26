package sort_algorithm;
import java.util.Random;

public class Selection {
	int intArray[];
	boolean sort = false;
	
	public Selection(int n) {//Array의 길이값을 입력 받아 길이에 해당하는 Array를 형성하고 랜덤값을 입력해준다.
		Random ran = new Random();
		intArray = new int[n];
		for(int i=0;i<this.intArray.length;i++)
			intArray[i]=ran.nextInt(100);
	}
	public void selecionSort() {
		for (int i=0;i<(this.intArray.length-1);i++) {
			int high = intArray[0];
			int highIndex = 0;
			for (int j=1;j<(this.intArray.length-i);j++) {
				if (this.intArray[j]>high) {
					high = this.intArray[j];
					highIndex = j;
				}
			} 
			int temp = this.intArray[this.intArray.length-1-i];//for문에서 확인했던 값 중 가장 오른쪽 값을 저장한다.
			this.intArray[this.intArray.length-1-i] = high;//가장 오른쪽 값에 가장 높은 값을 입력한다.
			this.intArray[highIndex] = temp;//가장 높은 값을 가졌던 곳에 가장 오른쪽 값을 넣어준다.
		} this.sort = true;
	}
	public void checkArray() {
		System.out.print("intArray : start -> ");
		for(int i=0;i<this.intArray.length;i++) {
			System.out.print(this.intArray[i]+" -> ");
		} System.out.println("end");
	}
	
	public static void main(String[] args) {
		Selection test = new Selection(10);
		test.checkArray();
		test.selecionSort();
		test.checkArray();
	}
}
