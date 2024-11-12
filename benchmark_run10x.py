test_range = 100000
# 1-100000 at 10 datas
test_10x(enhanced_insertion, "MB Sort", test_range, 10)
test_10x(insertionSort, "Insertion Sort", test_range, 10)

# 1-100000 at 1_000 datas
test_10x(enhanced_insertion, "MB Sort", test_range, 1_000)
test_10x(insertionSort, "Insertion Sort", test_range, 1_000)

# 1-100000 at 100_000 datas
test_10x(enhanced_insertion, "MB Sort", test_range, 100_000)
test_10x(insertionSort, "Insertion Sort", test_range, 100_000)

# 1-100000 at 1_000_000 datas
test_10x(enhanced_insertion, "MB Sort", test_range, 1_000_000)
test_10x(insertionSort, "Insertion Sort", test_range, 1_000_000)
