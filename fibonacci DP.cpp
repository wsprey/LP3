#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    if (n <= 0) return 0;

    vector<int> fib(n);
    fib[0] = 0;
    if (n > 1) fib[1] = 1;

    for (int i = 2; i < n; i++)
        fib[i] = fib[i - 1] + fib[i - 2];

    cout << "Fibonacci Series: ";
    for (int num : fib)
        cout << num << " ";

    cout << "\nFibonacci(" << n << ") = " << fib[n - 1] << endl;
    return 0;
}



# Fibonacci using Dynamic Programming (Tabulation)

n = int(input("Enter the number of elements: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    print("Fibonacci Series:", fib[:n])
    print(f"Fibonacci({n}) =", fib[n - 1])
