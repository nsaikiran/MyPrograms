package blog.saikiran.cache;

public class CacheElement<K ,V> {
    public K key;
    public V value;

    public CacheElement(K key, V value) {
        this.key = key;
        this.value = value;
    }

    @Override
    public String toString() {
        return key.toString() + ":" + value.toString();
    }
}