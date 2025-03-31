package blog.saikiran.ll;

public class DoublyLinkedList<T> {
    LinkedListNode<T> head;
    LinkedListNode<T> tail;

    public DoublyLinkedList() {
        head = null;
        tail = null;
    }

    public LinkedListNode<T> add(T data) {
        LinkedListNode<T> node = new LinkedListNode<T>(data);
        if (this.head == null ) {
            this.head = node;
            node.prev = null;
            node.next = null;
            this.tail = node;
            return node;
        }

        this.head.prev = node;
        node.next = this.head;
        node.prev = null;
        this.head = node;
        return node;
    }

    public  LinkedListNode<T> getTail() {
        return this.tail;
    }

    public void delete(LinkedListNode<T> node) {
        if (node == this.tail) {
            node.prev.next = null;
            this.tail = node.prev;
        }
        else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
    }

    public LinkedListNode<T> getHead() {
        return head;
    }

    public void printList() {
        LinkedListNode<T> temp = this.head;
        while (temp != null) {
            System.out.println(temp.getData());
            temp = temp.next;
        }
    }


    // public void updateAndMoveToHead(LinkedListNode<T> node) {
        
    //     // we can write one detach method then we can use
    // }

}