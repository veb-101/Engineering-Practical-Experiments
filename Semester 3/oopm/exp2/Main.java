import java.util.Scanner;
class Main{ 
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args){
	double a;
	System.out.println("enter radius");
	a = sc.nextDouble();
	Circle c1 = new Circle(a);
	Circle c2 = new Circle(c1);
	c1.print();
	c2.print();
	}
}

class Circle{ 
	double r,area;
	Circle (double r1){
		r = r1;
	}
	Circle (Circle c){
		r=c.r;
	}
	void print(){
		area = 3.14 * r* r;
		System.out.println("The area is :"+ area);
	}
}