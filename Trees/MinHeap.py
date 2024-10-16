import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print("Min-Heap:", [heapq.heappop(heap) for _ in range(len(heap))])