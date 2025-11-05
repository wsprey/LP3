#include <iostream>
#include <vector>
using namespace std;

// Recursive function to get nth Fibonacci number
int fib_recursive(int n) {
    if (n <= 1)
        return n;
    else
        return fib_recursive(n - 1) + fib_recursive(n - 2);
}

// Generate Fibonacci series using recursion
vector<int> fib_series_recursive(int n) {
    vector<int> series;
    for (int i = 0; i < n; i++)
        series.push_back(fib_recursive(i));
    return series;
}

// Non-recursive (iterative) function to get nth Fibonacci number
int fib_iterative(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// Generate Fibonacci series using iteration
vector<int> fib_series_iterative(int n) {
    vector<int> series;
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        series.push_back(a);
        int next = a + b;
        a = b;
        b = next;
    }
    return series;
}

// ---- Main Program ----
int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    // Recursive output
    cout << "\nUsing Recursive Method:\n";
    vector<int> rec_series = fib_series_recursive(n);
    cout << "Fibonacci Series: ";
    for (int num : rec_series)
        cout << num << " ";
    cout << "\nFibonacci(" << n << ") = " << fib_recursive(n - 1) << endl;

    // Iterative output
    cout << "\nUsing Non-Recursive (Iterative) Method:\n";
    vector<int> iter_series = fib_series_iterative(n);
    cout << "Fibonacci Series: ";
    for (int num : iter_series)
        cout << num << " ";
    cout << "\nFibonacci(" << n << ") = " << fib_iterative(n - 1) << endl;

    // ---- Time and Space Complexity ----
    cout << "\n--- Complexity Analysis ---\n";
    cout << "Recursive Approach:\n";
    cout << "  • Time Complexity  : O(2^n)\n";
    cout << "  • Space Complexity : O(n) (due to recursion stack)\n\n";
    cout << "Iterative Approach:\n";
    cout << "  • Time Complexity  : O(n)\n";
    cout << "  • Space Complexity : O(1)\n";

    return 0;
}
