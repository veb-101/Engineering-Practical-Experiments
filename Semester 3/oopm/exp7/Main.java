import java.util.Scanner;

class TestFinallyBlock{ 
    void TryCatchFinally(int data, boolean value){ 
         try{
			if(value){
            	data/=0;
			}
			else{
				data%= 10;
				System.out.println("Mod of value: " + data);
			}
            int arr[]={1,4,8};
            arr[9]=6;
        }
        catch(ArithmeticException e){
            System.out.println("Error:Divide by zero not allowed");
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Error:Array index out of bound");
        }
        finally{
            System.out.println("finally block is always executed");
        } 
        System.out.println("rest of the code..."); 
    } 
}

class TestThrow{ 
	void validate(int age){
		try{
        	if(age<18) 
        		throw new ArithmeticException("Using Throw KeyWord "); 
        	else 
        		System.out.println("welcome to vote"); 
    	}
		catch(ArithmeticException e){
		System.out.println("Caught: " + e.getClass() + e);
		}
	} 
} 

class TestThrows{
    void throws1() throws IllegalAccessException{
         System.out.println("Entered in throws1");
         throw new IllegalAccessException("Testing..");
    }
    void test(){
        try{
            System.out.println("Before throws1");
            throws1();
        }
        catch(IllegalAccessException e){
            System.out.println("Caught: "+e);
        }
    }
}


class Main {
  public static void main(String[] args) {
	System.out.println("Try Catch Finally......");
    TestFinallyBlock te = new TestFinallyBlock();
	te.TryCatchFinally(10, true);
	System.out.println("\n");
	te.TryCatchFinally(10, false);
	System.out.println("\n");
	System.out.println("Throw keyword....");
	TestThrow user = new TestThrow();
	user.validate(17);
	user.validate(20);
	System.out.println("\n");
	System.out.println("Throws keyword....");
	TestThrows tt = new TestThrows();
	tt.test();
	}
  }