import gov.nasa.jpf.symbc.Debug;

import java.util.Arrays;


public class BubbleSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BubbleSort bSort = new BubbleSort();
		bSort.runSort(1,2,3);
	}

    public String runSort(int val1, int val2, int val3)
    {

    	int[] inputArray = { val1, val2, val3};
    	int[] outputArray = this.bubbleSort(inputArray);
    	System.out.println("\n**************\n" + Arrays.toString(outputArray) + "\n");
    	Debug.printPC(Arrays.toString(outputArray));
    	System.out.println("\n**************\n");
    	return Arrays.toString(outputArray);

    }
    public int[] bubbleSort(int[] arrayIn) {

        // If array is null (None), return null (None)

    	//bubbleSort1
    	if(arrayIn == null)
    	{	//label: name=bubbleSort1
            return null;
    	}
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


}
