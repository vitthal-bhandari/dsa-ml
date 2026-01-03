"""
In this approach, we use Dijkstra's algorithm to find the minimum cost to create at least one valid path in the grid.

the weight of an edge is 0 if we follow the direction indicated by the cell, and 1 if we go against it.

Let n be the number of rows and m be the number of columns in the grid.

Time Complexity: O(n*m*log(n*m))

The algorithm uses Dijkstra's algorithm with a priority queue. In the worst case, we might need to visit each cell multiple times until we find the optimal path, but no more than 4 times per cell (once for each direction). For each cell, we perform a priority queue operation which takes O(log(n*m)) time, where n*m is the maximum size of the queue. Therefore, the total time complexity is O(n*m*log(n*m)).

Space Complexity: O(n*m)

The algorithm uses a priority queue that in the worst case might contain all cells of the grid, taking O(n*m) space.
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [(0, 0, 0)]
        visit=set()
        while minHeap:
            path, dx, dy = heapq.heappop(minHeap)
            if (dx, dy) == (nrows-1, ncols-1):
                return path
            if (dx, dy) in visit:
                continue
            visit.add((dx, dy))
            for d, (i, j) in enumerate(dirs):
                new_row, new_col = dx+i, dy+j
                if (new_row, new_col) not in visit and new_row in range(nrows) and new_col in range(ncols):
                    w = 0 if d == grid[dx][dy] - 1 else 1
                    heapq.heappush(minHeap, (w+path, new_row, new_col))
        return -1