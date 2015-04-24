import gov.nasa.jpf.symbc.Debug;

import java.util.Arrays;



public class MergeSort {
	InstrumentationClass rootNode;
	InstrumentationClass currentNode;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		MergeSort mSort = new MergeSort();
		mSort.runSort(1,2,3);
	}

    public String runSort(int val1, int val2, int val3)
    {
    	this.rootNode = new InstrumentationClass();
    	this.rootNode.NodeName = "C0";
    	this.currentNode = rootNode;
    	int[] inputArray = { val1, val2, val3};
    	int[] outputArray = this.mergeSort(inputArray);
    	System.out.println("\n**************\n" + Arrays.toString(outputArray) + "\n");
    	Debug.printPC(Arrays.toString(outputArray));
    	System.out.println("\n**************\n");
    	this.rootNode.printThis();
    	return Arrays.toString(outputArray);
    	
    }
    public int[] mergeSort(int[] arrayIn) {

        // If array is null (None), return null (None)
        if(arrayIn == null)
        {
        	InstrumentationClass arrayInNode = new InstrumentationClass();
            arrayInNode.NodeName = "C1";
            currentNode.nextNode = arrayInNode;
            currentNode = arrayInNode;
        	return null;
        }
        // If array size is 0 or 1, it is already sorted
        if(arrayIn.length < 2)
        {
        	InstrumentationClass arrayInNode = new InstrumentationClass();
            arrayInNode.NodeName = "C2";
            currentNode.nextNode = arrayInNode;
            currentNode = arrayInNode;
            return arrayIn;
        }
    	InstrumentationClass array2InNode = new InstrumentationClass();
        array2InNode.NodeName = "C3";
        currentNode.nextNode = array2InNode;
        currentNode = array2InNode;
        // Divide and conquer
        int index = arrayIn.length / 2;
        int[] a = new int[index];
        int[] b = new int[arrayIn.length-index];
        System.arraycopy(arrayIn, 0, a, 0, index);
        System.arraycopy(arrayIn, index, b, 0, arrayIn.length - index);
        a = this.mergeSort(a);
        b = this.mergeSort(b);

        // Needed variables
        int a_index = 0;
        int b_index = 0;
        int out_index = 0;
        int[] arrayOut = new int[a.length + b.length];

        // Sorting logic for ascending sort
        while(a_index < a.length && b_index < b.length) {
            if(a[a_index] > b[b_index]){
            	InstrumentationClass arrayInNode = new InstrumentationClass();
                arrayInNode.NodeName = "C4";
                currentNode.nextNode = arrayInNode;
                currentNode = arrayInNode;
                arrayOut[out_index] = b[b_index];
                b_index++;
            }
            else{
            	InstrumentationClass arrayInNode = new InstrumentationClass();
                arrayInNode.NodeName = "C5";
                currentNode.nextNode = arrayInNode;
                currentNode = arrayInNode;
                arrayOut[out_index] = a[a_index];
                a_index++;
            }
            out_index++;
        }

        if(a_index < b_index) {
            System.arraycopy(a, a_index, arrayOut, out_index,
                    arrayOut.length - out_index);
        	InstrumentationClass arrayInNode = new InstrumentationClass();
            arrayInNode.NodeName = "C6";
            currentNode.nextNode = arrayInNode;
            currentNode = arrayInNode;
        }
        else {
            System.arraycopy(b, b_index, arrayOut, out_index,
                    arrayOut.length - out_index);
        	InstrumentationClass arrayInNode = new InstrumentationClass();
            arrayInNode.NodeName = "C7";
            currentNode.nextNode = arrayInNode;
            currentNode = arrayInNode;
        }
        InstrumentationClass arrayIn3Node = new InstrumentationClass();
        arrayIn3Node.NodeName = "C8";
        currentNode.nextNode = arrayIn3Node;
        currentNode = arrayIn3Node;
        return arrayOut;
    }

}
