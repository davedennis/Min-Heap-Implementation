# Huffman-Coding
## Implemented methods
  - buildHeap()
  - heapify()
  - extrachMin()
  - heapInsert()
  - heapSort()
  
### How to run
  - Run the test program. It test all the implmented methods about and makes sure that the results are within a resonable complexity.
  - Example output
  '''
  (venv) C:\school\cs320\heapsRevistedPA3>heap_tests.py
#test_heapify
Heapify length 1: True
Heapify two out of order: True
Heapify two in order: True
Heapify five needing swap: True
Heapify five needing recursive swap: True
Heapify five with limit number: True
#test_build_heap
buildHeap(shuffled_list(5, 5)) is a min heap:  True
buildHeap(shuffled_list(10, 10)) is a min heap:  True
buildHeap(shuffled_list(15, 15)) is a min heap:  True
buildHeap(shuffled_list(20, 20)) is a min heap:  True
buildHeap(shuffled_list(25, 25)) is a min heap:  True
buildHeap(shuffled_list(30, 30)) is a min heap:  True
buildHeap(shuffled_list(35, 35)) is a min heap:  True
buildHeap(shuffled_list(40, 40)) is a min heap:  True
#test_insert_extract
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
Correctly extracted min: True, maintained heap property: True
#test_heap_sort:
Correctly sorted 1000 shuffled: True
#test_counts:
Counts for list of len: 400
buildHeap heapify calls within 20% of expected number of calls: True
heapExtractMin heapify calls within 20% of expected number of calls: True
heapInsert swap calls within 20% of expected number of calls: True
Counts for list of len: 10000
buildHeap heapify calls within 20% of expected number of calls: True
heapExtractMin heapify calls within 20% of expected number of calls: True
heapInsert swap calls within 20% of expected number of calls: True
Counts for list of len: 100000
buildHeap heapify calls within 20% of expected number of calls: True
heapExtractMin heapify calls within 20% of expected number of calls: True
heapInsert swap calls within 20% of expected number of calls: True

  '''
