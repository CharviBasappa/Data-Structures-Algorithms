import heapq

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(char_freq):
    heap = [Node(freq, char) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, new_node)

    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if node:
            if node.char:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + '0')
            generate_codes(node.right, current_code + '1')

    generate_codes(root, "")
    return codes

# Example usage
char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
print("Huffman Codes:", huffman_encoding(char_freq))
