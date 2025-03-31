package blog.saikiran.cache;

public interface Cache<K, V> {
    void put(K key, V value);
    boolean contains(K key); // wrap this using Optional
    V get(K key);

    boolean isEmpty();
    void clear();
}
