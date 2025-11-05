#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

class QuickSort {
private:
    int comparisons;
    int swaps;

    int partition(vector<int>& arr, int low, int high, bool randomized) {
        if (randomized) {
            int randomIndex = low + rand() % (high - low + 1);
            swap(arr[randomIndex], arr[high]);
            swaps++;
        }

        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            comparisons++;
            if (arr[j] <= pivot) {
                i++;
                swap(arr[i], arr[j]);
                swaps++;
            }
        }

        swap(arr[i + 1], arr[high]);
        swaps++;
        return i + 1;
    }

    void quickSort(vector<int>& arr, int low, int high, bool randomized) {
        if (low < high) {
            int pi = partition(arr, low, high, randomized);
            quickSort(arr, low, pi - 1, randomized);
            quickSort(arr, pi + 1, high, randomized);
        }
    }

public:
    void sortAndShow(vector<int> arr, bool randomized) {
        comparisons = 0;
        swaps = 0;

        clock_t start = clock();
        quickSort(arr, 0, arr.size() - 1, randomized);
        clock_t end = clock();

        double timeTaken = double(end - start) / CLOCKS_PER_SEC;

        cout << "\n" << (randomized ? "RANDOMIZED" : "DETERMINISTIC") << " QUICKSORT\n";
        cout << "Sorted array: [";
        for (size_t i = 0; i < arr.size(); i++) {
            cout << arr[i];
            if (i < arr.size() - 1) cout << ", ";
        }
        cout << "]\n";
        cout << "Comparisons: " << comparisons << endl;
        cout << "Swaps: " << swaps << endl;
        cout << "Time: " << timeTaken << " seconds\n";
    }
};

int main() {
    srand(time(0));

    cout << "Enter numbers separated by spaces: ";
    vector<int> arr;
    int num;
    while (cin >> num) {
        arr.push_back(num);
        if (cin.peek() == '\n') break;
    }

    if (arr.empty()) {
        cout << "Empty input!\n";
        return 0;
    }

    QuickSort sorter;
    sorter.sortAndShow(arr, false);  // Deterministic
    sorter.sortAndShow(arr, true);   // Randomized

    return 0;
}
