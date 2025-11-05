import random
import time

class QuickSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def partition(self, arr, low, high, randomized=False):
        if randomized:
            r = random.randint(low, high)
            arr[r], arr[high] = arr[high], arr[r]
            self.swaps += 1

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        return i + 1

    def quicksort(self, arr, low, high, randomized=False):
        if low < high:
            pi = self.partition(arr, low, high, randomized)
            self.quicksort(arr, low, pi - 1, randomized)
            self.quicksort(arr, pi + 1, high, randomized)

    def sort_and_analyze(self, arr, randomized=False):
        arr_copy = arr[:]
        self.comparisons = self.swaps = 0
        start = time.time()
        self.quicksort(arr_copy, 0, len(arr_copy) - 1, randomized)
        end = time.time()
        return arr_copy, self.comparisons, self.swaps, end - start

def main():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if not arr:
        print("Empty array!")
        return

    sorter = QuickSort()

    # Deterministic quicksort
    sorted_arr, comp, swp, t = sorter.sort_and_analyze(arr, False)
    print("\nDETERMINISTIC QUICKSORT")
    print("Sorted array:", sorted_arr)
    print(f"Comparisons: {comp}\nSwaps: {swp}\nTime: {t:.6f} s")

    # Randomized quicksort
    sorted_arr, comp, swp, t = sorter.sort_and_analyze(arr, True)
    print("\nRANDOMIZED QUICKSORT")
    print("Sorted array:", sorted_arr)
    print(f"Comparisons: {comp}\nSwaps: {swp}\nTime: {t:.6f} s")

if __name__ == "__main__":
    main()
