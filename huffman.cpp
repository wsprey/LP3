#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

// Node structure
struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = nullptr;
    }
};

// Compare structure for min-heap
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Generate Huffman codes
void generateCodes(Node* root, string code, unordered_map<char, string>& codes) {
    if (!root)
        return;
    if (root->ch != '\0')
        codes[root->ch] = code;

    generateCodes(root->left, code + "0", codes);
    generateCodes(root->right, code + "1", codes);
}

// Build Huffman Tree
Node* buildHuffmanTree(unordered_map<char, int>& freq) {
    priority_queue<Node*, vector<Node*>, Compare> pq;

    for (auto pair : freq)
        pq.push(new Node(pair.first, pair.second));

    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        Node* merged = new Node('\0', left->freq + right->freq);
        merged->left = left;
        merged->right = right;

        pq.push(merged);
    }

    return pq.top();
}

// ---- Main Program ----
int main() {
    string text;
    cout << "Enter a string: ";
    getline(cin, text);

    unordered_map<char, int> freq;
    for (char ch : text)
        freq[ch]++;

    Node* root = buildHuffmanTree(freq);

    unordered_map<char, string> codes;
    generateCodes(root, "", codes);

    cout << "\nHuffman Codes:\n";
    for (auto pair : codes)
        cout << pair.first << ": " << pair.second << endl;

    cout << "\nEncoded Text: ";
    for (char ch : text)
        cout << codes[ch];
    cout << endl;

    return 0;
}
