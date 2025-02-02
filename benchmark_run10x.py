from timeit import timeit
import random
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion

n = 10_000
r = 10

arr1 = random.choices(range(1, r), k = n)

t1 = timeit(
    "insertionSort(arr1)",
    setup="from normal_algo.insertion_sort import insertionSort",
    number = 1,
    globals={"arr1":arr1},
)

def test_10x(func, name, r, n):
    print(f"Benchmark for {name} \n@ {n} datas ranging from 1 - {r}")
    for i in range(1,11):
        arr1 = random.choices(range(1, r), k = n)
        t1 = timeit(
        lambda: func(arr1),
        number = 1,
        globals={"arr1": arr1, "func": func},
        )
        print(f"{t1}")
    print()

# 1-10 at 10 datas
test_10x(enhanced_insertion, "MB Sort", 10, 10)
test_10x(insertionSort, "Insertion Sort", 10, 10)

# 1-10 at 1_000 datas
test_10x(enhanced_insertion, "MB Sort", 10, 10)
test_10x(insertionSort, "Insertion Sort", 10, 10)

# 1-10 at 100_000 datas
test_10x(enhanced_insertion, "MB Sort", 10, 10)
test_10x(insertionSort, "Insertion Sort", 10, 10)

# 1-10 at 1_000_000 datas
test_10x(enhanced_insertion, "MB Sort", 10, 10)
test_10x(insertionSort, "Insertion Sort", 10, 10)
