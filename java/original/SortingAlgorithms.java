import java.lang.System;
import java.util.Arrays;

/**
 * SortingAlgorithms
 * -------------------------------------------------------------------------
 * Contains java implementations of bubble sort, merge sort, and quick sort.
 * Created by AWood on 2015-03-10.
 */
public class SortingAlgorithms {

    public static void main(String args[]){
        int[] inputArray = {5, 4, 1, 2, 3};
        int[] outputArray = QuickSort(inputArray);
        System.out.println(Arrays.toString(outputArray));
    }

    public static int[] BubbleSort(int[] arrayIn) {

        // If array is null (None), return null (None)
        if(arrayIn == null)
            return null;

        // If array size is 0 or 1, it is already sorted
        if(arrayIn.length < 2)
            return arrayIn;

        for(int i=0; i < arrayIn.length-1; i++){
            for(int j=0; j < arrayIn.length-1; j++) {
                if (arrayIn[j] > arrayIn[j+1]) {
                    int temp = arrayIn[j+1];
                    arrayIn[j+1] = arrayIn[j];
                    arrayIn[j] = temp;
                }
            }
        }

        return arrayIn;
    }

    public static int[] MergeSort(int[] arrayIn) {

        // If array is null (None), return null (None)
        if(arrayIn == null)
            return null;

        // If array size is 0 or 1, it is already sorted
        if(arrayIn.length < 2)
            return arrayIn;

        // Divide and conquer
        int index = arrayIn.length / 2;
        int[] a = new int[index];
        int[] b = new int[arrayIn.length-index];
        System.arraycopy(arrayIn, 0, a, 0, index);
        System.arraycopy(arrayIn, index, b, 0, arrayIn.length - index);
        a = MergeSort(a);
        b = MergeSort(b);

        // Needed variables
        int a_index = 0;
        int b_index = 0;
        int out_index = 0;
        int[] arrayOut = new int[a.length + b.length];

        // Sorting logic for ascending sort
        while(a_index < a.length && b_index < b.length) {
            if(a[a_index] > b[b_index]){
                arrayOut[out_index] = b[b_index];
                b_index++;
            }
            else{
                arrayOut[out_index] = a[a_index];
                a_index++;
            }
            out_index++;
        }

        if(a_index < b_index) {
            System.arraycopy(a, a_index, arrayOut, out_index,
                    arrayOut.length - out_index);
        }
        else {
            System.arraycopy(b, b_index, arrayOut, out_index,
                    arrayOut.length - out_index);
        }

        return arrayOut;
    }

    public static int[] QuickSort(int[] arrayIn) {

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
        int[] lesser = QuickSort(a);
        int[] greater = QuickSort(b);

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
