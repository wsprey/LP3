import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operator for min-heap
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # root node


# Generate Huffman Codes
def generate_codes(root, code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code
    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)
    return codes


# ---- Main Program ----
text = input("Enter a string: ")

# Calculate frequency of each character
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Build Huffman Tree
root = build_huffman_tree(freq)

# Generate Huffman Codes
codes = generate_codes(root)

# Print codes
print("\nHuffman Codes:")
for ch in codes:
    print(f"{ch}: {codes[ch]}")

# Encode input text
encoded_text = ''.join(codes[ch] for ch in text)
print("\nEncoded Text:", encoded_text)
