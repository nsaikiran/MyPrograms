/*
LRU Cache 
*/
package blog.saikiran.driver;

import blog.saikiran.lru.*;

public class LRUCacheDriver {
    public static void main(String[] args) {
        LRUCache<Integer, String> lCache = new LRUCache<>();
       //lCache.printElements();
        lCache.put(0, "Saikiran");
        //lCache.printElements();
        lCache.put(1, "Boss");
        lCache.put(2, "Cmndr");
        lCache.put(3, "Hero");
        lCache.put(4, "Artist");
        lCache.printElements();
        lCache.put(5, "King");
        lCache.printElements();
    }
}