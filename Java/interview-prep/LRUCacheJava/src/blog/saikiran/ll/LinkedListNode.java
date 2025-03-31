package blog.saikiran.ll;

public class LinkedListNode<T> {
    LinkedListNode<T> next;
    LinkedListNode<T> prev;
    T data;

    LinkedListNode(T data) {
        this.data = data;
        next = null;
        prev = null;
    }

    public T getData() {
        return data;
    }

    // public LinkedListNode<T> getNext() {
    //     return next;
    // }
    //  public LinkedListNode<T> getPrev() {
    //     return prev;
    // }
}