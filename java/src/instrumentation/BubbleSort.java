import gov.nasa.jpf.symbc.Debug;

import java.util.Arrays;


public class BubbleSort {
	public InstrumentationClass rootNode;
	public InstrumentationClass currentNode;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BubbleSort bSort = new BubbleSort();
		bSort.runSort(1,2,3);
	}

    public String runSort(int val1, int val2, int val3)
    {
    	this.rootNode = new InstrumentationClass();
    	this.rootNode.NodeName = "C0";
    	this.currentNode = rootNode;
    	
    	

    	int[] inputArray = { val1, val2, val3};
    	int[] outputArray = this.bubbleSort(inputArray);
    	System.out.println("\n**************\n" + Arrays.toString(outputArray) + "\n");
    	Debug.printPC(Arrays.toString(outputArray));
    	System.out.println("\n**************\n");
    	this.rootNode.printThis();
    	return Arrays.toString(outputArray);
    	
    }
    public int[] bubbleSort(int[] arrayIn) {

        // If array is null (None), return null (None)
        
    	//bubbleSort1
    	if(arrayIn == null)
    	{	//label: name=bubbleSort1
            
            InstrumentationClass arrayIn3Node = new InstrumentationClass();
            arrayIn3Node.NodeName = "C1";
            currentNode.nextNode = arrayIn3Node;
            currentNode = arrayIn3Node;
            return null;
    	}
        // If array size is 0 or 1, it is already sorted
        if(arrayIn.length < 2)
        {
        	
            InstrumentationClass arrayIn3Node = new InstrumentationClass();
            arrayIn3Node.NodeName = "C2";
            currentNode.nextNode = arrayIn3Node;
            currentNode = arrayIn3Node;
            return arrayIn;
        }
        
        InstrumentationClass arrayIn2Node = new InstrumentationClass();
        arrayIn2Node.NodeName = "C3";
        currentNode.nextNode = arrayIn2Node;
        currentNode = arrayIn2Node;
        
        for(int i=0; i < arrayIn.length - (i + 1); i++){
            for(int j=0; j < arrayIn.length-1; j++) {
                if (arrayIn[j] > arrayIn[j+1]) {
                    int temp = arrayIn[j+1];
                    arrayIn[j+1] = arrayIn[j];
                    arrayIn[j] = temp;
                    InstrumentationClass arrayIn1Node = new InstrumentationClass();
                    arrayIn1Node.NodeName = "C4";
                    currentNode.nextNode = arrayIn1Node;
                    currentNode = arrayIn1Node;
                }
                else
                {
                	InstrumentationClass arrayIn12Node = new InstrumentationClass();
                    arrayIn12Node.NodeName = "C5";
                    currentNode.nextNode = arrayIn12Node;
                    currentNode = arrayIn12Node;
                }
            }
        }
        
        InstrumentationClass arrayInNode = new InstrumentationClass();
        arrayInNode.NodeName = "C6";
        currentNode.nextNode = arrayInNode;
        currentNode = arrayInNode;

        return arrayIn;
    }
	
	
}
