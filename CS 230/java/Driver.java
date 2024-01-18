public class Driver {
  public static void main(String[] args) {
    IntList a = new IntList(null);
    IntList b = a.cons(2);
    IntList c = b.cons(1);
    int x = a.length() + b.length() + c.length();
    a.print();
    b.print();
    c.print();
    System.out.println(x);
    System.out.println(a.length_r() + " " + c.length_r());
    System.out.println(a.contains(1) + " " + c.contains(1) + " " + c.contains(2) + " " + c.contains(3));
    System.out.println(a.contains_r(1) + " " + c.contains_r(1) + " " + c.contains_r(2) + " " + c.contains_r(3));
  }
}