package blog.saikiran.lru;

import java.util.*;

import blog.saikiran.cache.Cache;
import blog.saikiran.cache.CacheElement;

import blog.saikiran.ll.LinkedListNode;
import blog.saikiran.ll.DoublyLinkedList;


public class LRUCache<K, V> implements Cache<K, V> {
    private static int MAX_SIZE = 5;
    private int size;

    Map<K, LinkedListNode<CacheElement<K, V>>> linkedListNodeMap;
    DoublyLinkedList<CacheElement<K, V>> linkedList;

    public LRUCache() {
        size = 0;
        this.linkedListNodeMap = new HashMap<>();
        this.linkedList = new DoublyLinkedList<>();
    }

    public void clear() {
        //clear map
        // claer ll;
    }

    public boolean isEmpty() {
        // stub
        return false;
    }

    public V get(K key) {
        return linkedListNodeMap.get(key).getData().value;
    }

    public boolean contains(K key) {
        return linkedListNodeMap.containsKey(key);
    }

    // LRU is strategy. Least Recently Used is at the tail.
    void evitItemPerStrategy() {
        LinkedListNode<CacheElement<K, V>> tail = linkedList.getTail();
        K key = tail.getData().key;
        // remove from map
        linkedListNodeMap.remove(key);
        // remove rom LL
        linkedList.delete(tail);
        size -= 1;
    }

    public void put(K key, V value) {
        System.out.println("Size:" + size);
        if (size == LRUCache.MAX_SIZE) {
            evitItemPerStrategy();
        }
        CacheElement<K, V> cacheElement = new CacheElement<K, V>(key, value);
        if (linkedListNodeMap.containsKey(key)) {
            //update the DLL to move this to front.
            LinkedListNode<CacheElement<K, V>> node = linkedListNodeMap.get(key);
            linkedList.delete(node);
        }
        LinkedListNode<CacheElement<K, V>> llNode = linkedList.add(cacheElement);
        linkedListNodeMap.put(key, llNode);
        size += 1;
    }

    public void printElements() {
        System.out.println("\nprintElements");
        for (Map.Entry<K, LinkedListNode<CacheElement<K, V>>> entry: linkedListNodeMap.entrySet()) {
            K key = entry.getKey();
            CacheElement<K, V> element = entry.getValue().getData();
            System.out.println(element.key + ":" +element.value);
        }
        System.out.println("\nSeperator");
        linkedList.printList();
    }

}
