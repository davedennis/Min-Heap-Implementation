import sys
import math

# BEGIN DO NOT MODIFY

db = False
swap_count = 0
heapify_call_count = 0


def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0

    
def swap(A, i, j):
    global swap_count
    swap_count += 1
    A[i], A[j] = A[j], A[i]

    
def count_heapify():
    global heapify_call_count
    heapify_call_count += 1

    
def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}


def readNums(filename):
    """Reads a text file containing whitespace separated numbers.
    Returns a list of those numbers."""
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        if db:
            print("List read from file {}: {}".format(filename, lst))
        return lst

    
# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

# END DO NOT MODIFY

def heapify(A, i, n=None):
    count_heapify()
    if n is None:
        n = len(A)
    if not(i < n):
        return

    l = left(i)
    r = right(i)
    smallest = i
    #check left root child
    if l < n and A[l] < A[smallest]:
        smallest = l
    #check right root child
    if r < n and A[r] < A[smallest]:
        smallest = r
    #swap and recure
    if smallest != i:
        #A[i], A[smallest] = A[smallest], A[i]
        swap(A,i,smallest)
        heapify(A, smallest, n)
    


def buildHeap(A):
    n = len(A)
    for i in range(int(n/2) , -1 , -1):
        heapify(A, i , n)
    


def heapExtractMin(A):
    min = A[0]
    #A[0], A[len(A)-1] = A[len(A)-1], A[0]
    swap(A, 0, len(A)-1)
    A.pop(len(A) - 1)
    heapify(A,0,len(A))
    return min



def heapInsert(A, v):
    if len(A) == 0:
        A.append(v)
    else:
        A.append(v)
        #need to bubble_up here since it's not the first element
        start = len(A) - 1
        while start > 0 and A[parent(start)] > A[start]:
            x = A[start]
            #A[start], A[parent(start)] = A[parent(start)], A[start]
            swap(A, start, parent(start))
            start = parent(start)



def heapSort(A):
    buildHeap(A)
    start = len(A)
    end = len(A) - 1
    for i in range(start, 0, -1):
        #A[0], A[end] = A[end], A[0]
        swap(A, 0, end)
        heapify(A, 0, end)
        end = end - 1



def printHeap(A):
    height = int(math.log(len(A), 2))
    width = len(str(max(A)))
    for i in range(height + 1):
        print(width * (2 ** (height - i) - 1) * " ", end="")
        for j in range(2 ** i):
            idx = 2 ** i - 1 + j
            if idx >= len(A):
                print()
                break
            if j == 2 ** i - 1:
                print("{:^{width}}".format(A[idx], width=width))
            else:
                print("{:^{width}}".format(A[idx], width=width),
                      width * (2 ** (height - i + 1) - 1) * " ", sep='', end='')
    print()


def shuffled_list(length, seed):
    A = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(A)
    return A


def report_counts_on_basic_ops(A, loop_extracts=1, loop_inserts=1):
    original_len = len(A)
    print("\nREPORT on list of len: {}".format(original_len))
    reset_counts()
    buildHeap(A)
    print("buildHeap(A):           \t", current_counts())

    reset_counts()
    m = heapExtractMin(A)
    print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    reset_counts()
    heapInsert(A, m)
    print("heapInsert(A, {}):       \t".format(m), current_counts())

    for i in range(loop_extracts):
        reset_counts()
        m = heapExtractMin(A)
        print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    import random
    r = random.Random(0)
    for i in range(loop_inserts):
        reset_counts()
        new_number = r.randrange(0, original_len // 8)
        heapInsert(A, new_number)
        print("heapInsert(A, {}):       \t".format(new_number), current_counts())


def main():
    global db
    if len(sys.argv) > 2:
        db = True
    
    A = shuffled_list(30, 0)
    report_counts_on_basic_ops(A)
    
    A = shuffled_list(400, 0)
    report_counts_on_basic_ops(A)
    
    A = shuffled_list(10000, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(100000, 0)
    report_counts_on_basic_ops(A, 3, 3)

if __name__ == "__main__":
    main()
