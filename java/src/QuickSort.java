import gov.nasa.jpf.symbc.Debug;

import java.util.Arrays;


public class QuickSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		QuickSort qSort = new QuickSort();
		qSort.runSort(1,2,3);
	}

    public String runSort(int val1, int val2, int val3)
    {

    	int[] inputArray = { val1, val2, val3};
    	int[] outputArray = this.quickSort(inputArray);
    	System.out.println("\n**************\n" + Arrays.toString(outputArray) + "\n");
    	Debug.printPC(Arrays.toString(outputArray));
    	System.out.println("\n**************\n");
    	return Arrays.toString(outputArray);

    }

	   public int[] quickSort(int[] arrayIn) {

	        // If array is null (None), return null (None)
	        if(arrayIn == null)
	            return null;

	        // If array size is 0 or 1, it is already sorted
	        if(arrayIn.length < 2)
	            return arrayIn;

	        int max_index = arrayIn.length - 1;
	        int index = partition(arrayIn, 0, max_index);

	        int[] a = new int[index + 1];
	        int[] b = new int[max_index - index];
	        System.arraycopy(arrayIn, 0, a, 0, index + 1);
	        System.arraycopy(arrayIn, index + 1, b, 0, arrayIn.length - index - 1);
	        int[] lesser = this.quickSort(a);
	        int[] greater = this.quickSort(b);

	        System.arraycopy(lesser, 0, arrayIn, 0, lesser.length);
	        System.arraycopy(greater, 0, arrayIn, lesser.length, greater.length);

	        return arrayIn;
	    }

	    public static int partition(int[] arrayIn, int min_index, int max_index){
	        int pivot_index = choosePivot(min_index, max_index);
	        int pivot_value = arrayIn[pivot_index];
	        swap(arrayIn, pivot_index, max_index);
	        int return_index = min_index;
	        for (int i = min_index; i < max_index; i++) {
	            if(arrayIn[i] < pivot_value) {
	                swap(arrayIn,i,return_index);
	                return_index++;
	            }
	        }
	        swap(arrayIn, return_index, max_index);
	        return return_index;
	    }

	    public static int choosePivot(int min_index, int max_index) {
	        return (min_index + max_index) / 2;
	    }

	    public static void swap(int[] arrayIn, int a, int b){
	        int temp = arrayIn[a];
	        arrayIn[a] = arrayIn[b];
	        arrayIn[b] = temp;
	    }

}
