package sort_algorithm;
import java.util.Random;

public class Selection {
	int intArray[];
	boolean sort = false;
	
	public Selection(int n) {//Array�� ���̰��� �Է� �޾� ���̿� �ش��ϴ� Array�� �����ϰ� �������� �Է����ش�.
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
			int temp = this.intArray[this.intArray.length-1-i];//for������ Ȯ���ߴ� �� �� ���� ������ ���� �����Ѵ�.
			this.intArray[this.intArray.length-1-i] = high;//���� ������ ���� ���� ���� ���� �Է��Ѵ�.
			this.intArray[highIndex] = temp;//���� ���� ���� ������ ���� ���� ������ ���� �־��ش�.
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
