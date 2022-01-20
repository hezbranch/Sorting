# Sorting
Implementation of sorting algorithms from Introduction to Algorithms (CLRS)

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms. MIT press.
Chicago	

**Command line tutorial for Insertion Sort:**

\>>> from InsertionSort import \* <br/>
\>>> unsorted = [1, 5, 3, -1, 0, 9, 12] <br/>
\>>> sort = InsertionSort(unsorted)<br/>
\>>> sort.sort()<br/>
[-1, 0, 1, 3, 5, 9, 12]<br/>
\>>> sort.swap(2, 4)<br/>
[-1, 0, 5, 3, 1, 9, 12]<br/>
\>>> sort.sort()<br/>
[-1, 0, 1, 3, 5, 9, 12]<br/>
