# Sorting
Implementation of sorting algorithms from Introduction to Algorithms (CLRS)

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms. MIT press.	

## Getting Started

*Command line tutorial for Insertion Sort:*

\>>> from InsertionSort import \* <br/>
\>>> unsorted = [1, 5, 3, -1, 0, 9, 12] <br/>
\>>> test = InsertionSort(unsorted)<br/>
\>>> test.sort()<br/>
[-1, 0, 1, 3, 5, 9, 12]<br/>
\>>> test.swap(2, 4)<br/>
[-1, 0, 5, 3, 1, 9, 12]<br/>
\>>> test.sort()<br/>
[-1, 0, 1, 3, 5, 9, 12]<br/>
\>>> test.time_it()<br/>
0.000028849 seconds <br/>

## Next Steps

Hoping to add MergeSort, Quicksort, and a brief discussion on best use-cases.

Optimistically, an example of a quantum sorting algorithm (for space complexity analysis).
