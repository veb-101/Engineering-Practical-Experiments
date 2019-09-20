import java.util.Scanner;


class Main1 {
	static Scanner sc = new Scanner(System.in);
	public static void main (String [] args) {
	System.out.println("Enter the number of element:");
    int n = sc.nextInt();
	System.out.println("Enter array of numbers:");
	int[] array = new int[n];
	for (int j = 0; j < n; j++){
        array[j] = sc.nextInt();
    }

   	int temp;
   	for (int i = 1; i < array.length; i++) {
    	for (int j = i; j > 0; j--) {
     		if (array[j] < array [j - 1]) {
      			temp = array[j];
      			array[j] = array[j - 1];
      			array[j - 1] = temp;
     		}
    	}
   	}
   	System.out.print("Ascending order: ");
   	for (int i = 0; i < array.length; i++) {
    	System.out.print(array[i] + " ");
	   }
	System.out.print("\nDescending order: ");
   	for (int i = n-1; i>=0; i--) 
    	System.out.print(array[i] + " ");
	System.out.println("\n");
	}
}
 
public class Main{
	static Scanner input = new Scanner(System.in);
    public static void main(String args[]){
        int n;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the base of squared matrices");
        n = input.nextInt();
        int[][] a = new int[n][n];
        int[][] b = new int[n][n];
        int[][] c = new int[n][n];
        System.out.println("Enter the elements of 1st martix row wise \n");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                a[i][j] = input.nextInt();
            }
        }
        System.out.println("Enter the elements of 2nd martix row wise \n");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                b[i][j] = input.nextInt();
            }
        }
        System.out.println("Multiplying the matrices...");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                for (int k = 0; k < n; k++)
                {
                    c[i][j] = c[i][j] + a[i][k] * b[k][j];
                }
            }
        }
        System.out.println("The product is:");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
        input.close();
    }
}