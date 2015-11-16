import MyPack.BubbleSort;
public class UseBubbleSort{
	public static void main(String[] args){
		int[] list={3,0,8,3,23,6,123,4,6,-1};
		BubbleSort.sort(list);
		for (int var=0;var<list.length;++var)
			System.out.println(list[var]);
		}
	}
