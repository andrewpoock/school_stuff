/**
 * An IntList is a list of ints.
 */
public class IntList {
  private ConsCell start; // first in the list or null

  /**
   * Construct a new IntList given its first ConsCell.
   * @param s the first ConsCell in the list or null
   */
   public IntList(ConsCell s) {
    start = s;
  }

  /**
   * Cons the given element h onto us and return the
   * resulting IntList.
   * @param h the head int for the new list
   * @return the IntList with head h and us for a tail
   */
  public IntList cons (int h) {
    return new IntList(new ConsCell(h,start));
  }

  /**
   * Get our length.
   * @return our int length
   */
  public int length() {
    int len = 0;
    ConsCell cell = start;
    while (cell != null) { // while not at end of list
      len++;
      cell = cell.getTail();
    }
    return len;
  }

  public int length_r() {
    if (start == null) {
      return 0;
    }
    return start.length();
  }

  public boolean contains(int n) {
    /*ConsCell cell = start;
    while (cell != null) {
      if (cell.getHead() == n) {
        return true;
      }
      cell = cell.getTail();
    }
    return false;*/
    for (ConsCell cell = start; cell != null; cell = cell.getTail()) {
      if (cell.getHead() == n) {
        return true;
      }
    }
      return false;
  }

  public boolean contains_r(int n) {
    return start != null && start.contains(n);
  }

  /**
   * Print ourself to System.out.
   */
  public void print() {
    System.out.print("[");
    ConsCell a = start;
    while (a != null) {
      System.out.print(a.getHead());
      a = a.getTail();
      if (a != null) System.out.print(",");
    }
    System.out.println("]");
  }
}

