import org.junit.Assert;
import org.junit.Test;

/**
 * TestSortingAlgorithms
 * --------------------------------------------------------------------------------
 * A test suite to provide sanity checks for the sorting algorithms. Tests include:
 *     - Test against null
 *     - Test against empty set
 *     - Test against sorted array
 *    - Test against unsorted array
 *    - Test against uniform array
 *
 * Created by AWood on 2015-03-10.
 */
public class TestSortingAlgorithms {

    @Test public void testBSNull(){
        Assert.assertNull(SortingAlgorithms.BubbleSort(null));
    }

    @Test public void testMSNull(){
        Assert.assertNull(SortingAlgorithms.MergeSort(null));
    }

    @Test public void testQSNull(){
        Assert.assertNull(SortingAlgorithms.QuickSort(null));
    }

    @Test public void testBSEmptyArray(){
        int[] test_input = {};
        int[] test_output = SortingAlgorithms.BubbleSort(test_input);
        Assert.assertEquals(test_input, test_output);
    }

    @Test public void testMSEmptyArray(){
        int[] test_input = {};
        int[] test_output = SortingAlgorithms.MergeSort(test_input);
        Assert.assertEquals(test_input, test_output);
    }

    @Test public void testQSEmptyArray(){
        int[] test_input = {};
        int[] test_output = SortingAlgorithms.QuickSort(test_input);
        Assert.assertEquals(test_input, test_output);
    }

    @Test public void testBSSortingSortedArray(){
        int[] test_input = {0, 1, 2, 3, 4, 5};
        int[] test_output = SortingAlgorithms.BubbleSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testMSSortingSortedArray(){
        int[] test_input = {0, 1, 2, 3, 4, 5};
        int[] test_output = SortingAlgorithms.MergeSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testQSSortingSortedArray(){
        int[] test_input = {0, 1, 2, 3, 4, 5};
        int[] test_output = SortingAlgorithms.QuickSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testBSSortingUnsortedArray(){
        int[] test_input = {5, 3, 1, 4, 2, 0};
        int[] test_output = SortingAlgorithms.BubbleSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testMSSortingUnsortedArray(){
        int[] test_input = {5, 3, 1, 4, 2, 0};
        int[] test_output = SortingAlgorithms.MergeSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testQSSortingUnsortedArray(){
        int[] test_input = {5, 3, 1, 4, 2, 0};
        int[] test_output = SortingAlgorithms.QuickSort(test_input);
        Assert.assertArrayEquals(new int[] {0, 1, 2, 3, 4, 5}, test_output);
    }

    @Test public void testBSSortingUniform(){
        int[] test_input = {1, 1, 1, 1, 1, 1};
        int[] test_output = SortingAlgorithms.BubbleSort(test_input);
        Assert.assertArrayEquals(new int[] {1, 1, 1, 1, 1, 1}, test_output);
    }

    @Test public void testMSSortingUniform(){
        int[] test_input = {1, 1, 1, 1, 1, 1};
        int[] test_output = SortingAlgorithms.MergeSort(test_input);
        Assert.assertArrayEquals(new int[] {1, 1, 1, 1, 1, 1}, test_output);
    }

    @Test public void testQSSortingUniform(){
        int[] test_input = {1, 1, 1, 1, 1, 1};
        int[] test_output = SortingAlgorithms.QuickSort(test_input);
        Assert.assertArrayEquals(new int[] {1, 1, 1, 1, 1, 1}, test_output);
    }
}
