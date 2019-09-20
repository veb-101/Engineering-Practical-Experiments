class Odd extends Thread{
		public Odd(String n){
			super(n);
			start();
		}
		public void run(){
			for(int i = 1; i<=20;i=i+2){
				System.out.println(getName() + "="+ i);
				try{
					Thread.sleep(500);
				}
				catch(Exception e){
					System.out.println(e);
				}
			}
		}
}

class Even extends Thread{
		public Even(String n){
			super(n);
			start();
		}
		public void run(){
			for(int i = 0; i<=20;i=i+2){
				System.out.println(getName() + "="+ i);
				try{
					Thread.sleep(500);
				}
				catch(Exception e){
					System.out.println(e);
				}
			}
		}
}

class Main {
  public static void main(String[] args) {
	  Odd o = new Odd("Thread1:");
	  Even e = new Even("Thread2:");
	}
}