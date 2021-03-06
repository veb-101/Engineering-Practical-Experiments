import java.util.Vector;
class Main{ 
    public static void main(String[] arg){ 
        Vector v = new Vector(10); 
		v.add(new Integer(1));
        v.addElement(new Integer(2)); 
		v.addElement(new Character('A'));
		v.addElement(new Boolean(true));
        v.addElement(new String("Test1"));
        v.addElement(new String("Remove1"));
		v.addElement(new String("Remove2")); 
        System.out.println("Vector is: " + v); 
		v.removeElement(new String("Remove1"));
        System.out.println("Vector is: " + v); 
		v.removeElementAt(5);
		System.out.println("Vector is: " + v); 
		v.insertElementAt(new String("New"), 5);
		System.out.println("Vector is: " + v);
		System.out.println("Vector size: " + v.size());
		System.out.println("Vector capacity: " + v.capacity());
    } 
}