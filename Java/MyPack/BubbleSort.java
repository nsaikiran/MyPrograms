package MyPack;
public class BubbleSort {
	public static void sort(int[] array){
		int temp;
		for (int var=0;var< array.length;++var){
			for (int flag=0;flag<array.length-1;++flag){
				if (array[flag] > array[flag+1]){
					temp=array[flag];
					array[flag]=array[flag+1];
					array[flag+1]=temp;
					}
				}
			}	
		}
	
	}
