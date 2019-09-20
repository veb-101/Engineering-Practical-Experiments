import java.util.Scanner;
class sub_marks{
	static Scanner sc = new Scanner(System.in);
	int m1, m2;
	void getMarks(){
		System.out.print("Enter TT-1 marks: ");
		m1 = sc.nextInt();
		System.out.print("Enter TT-2 marks: ");
		m2 = sc.nextInt();
		System.out.println();
	}
}

 interface NSS{
	final  int B_marks = 10;
  	static void show(){}
}

class Total extends sub_marks implements NSS{
	int total;
	void show(){
		getMarks();
		total = m1 + m2 + B_marks;
		System.out.println("----Details----");
		System.out.println("TT-1 Marks: " + m1);
		System.out.println("TT-2 Marks: " + m2);
		System.out.println("Total Marks (+NSS marks): " + total);
		System.out.println("Percentage: " + (total * 100)/ 50 + "%");
	}
}
class Main {
	public static void main(String[] args) {
		Total tt = new Total();
		tt.show();
	}
}