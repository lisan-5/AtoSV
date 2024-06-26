class Solution:
    def kClosest(self, points, k):
        def distance(point):
            x, y = point
            return x**2 + y**2
        
        max_heap = []
        for x, y in points:
            dist = -distance((x, y))
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                heapq.heappushpop(max_heap, (dist, x, y))
        
        return [(x, y) for (dist, x, y) in max_heap]
