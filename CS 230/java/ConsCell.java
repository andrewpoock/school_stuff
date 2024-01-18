/**
 * A ConsCell is an element in a linked list of
 * ints.
 */
public class ConsCell {
  private int head; // the first item in the list
  private ConsCell tail; // rest of the list or null

  /** 
   * Construct a new ConsCell given its head and tail.
   * @param h the int contents of this cell
   * @param t the next ConsCell in the list or null
   */
  public ConsCell(int h, ConsCell t) {
    head = h;
    tail = t;
  }
  /**
   * Accessor for the head of this ConsCell.
   * @return the int contents of this cell
   */
  public int getHead() {
    return head;
  }

  /**
   * Accessor for the tail of this ConsCell.
   * @return the next ConsCell in the list or null
   */
  public ConsCell getTail() {
    return tail;
  }

  /**
   * Mutator for the tail of this ConsCell.
   * @param t the new tail for this cell
   */
  public void setTail(ConsCell t) {
    tail = t;
  }

  public int length() {
    if (tail == null) {
      return 1;
    }
    return tail.length() + 1;
  }

  public boolean contains(int n) {
    return head == n || (tail != null && tail.contains(n));
  }
  
}
