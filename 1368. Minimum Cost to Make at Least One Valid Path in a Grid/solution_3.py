"""
In this approach we use 0-1 BFS to find the minimum cost to create at least one valid path in the grid.

In 0-1 BFS, we adjust the traditional BFS by using a deque (double-ended queue) instead of a regular queue. The deque allows us to prioritize 0-cost edges more efficiently. Each element of the deque will store the row and column indices of a cell, and we will maintain a minCost grid to track the minimum cost to reach each cell.

As we visit each cell, we evaluate its four neighboring cells. If moving to a neighbor doesn't require a sign change (i.e., the move is a 0-cost move), we add that neighbor to the front of the deque because we want to explore it immediately. On the other hand, if a sign change is required (making it a 1-cost move), we add the neighbor to the back of the deque, ensuring it gets explored later, after all the 0-cost moves.

For each neighbor we explore, we calculate the cost to reach it and compare it to the current value in the minCost grid. If the calculated cost is lower, we update minCost with the new, cheaper value.

Once the BFS traversal completes and all cells have been processed, the minimum cost to reach the bottom-right corner will be stored in minCost. We return this value as the solution to the problem.

Let n be the number of rows and m be the number of columns in the grid.

Time Complexity: O(n*m)

The algorithm uses 0-1 BFS approach where each cell is visited at most once for each edge weight (0 or 1). Since we process zero-weight edges before one-weight edges (by adding to the front of the deque), each cell gets its final shortest distance when it's first processed. No cell is processed more than once with the same cost. Therefore, the time complexity is linear with respect to the number of cells, giving us O(n*m).

Space Complexity: O(n*m)

The algorithm uses a deque that in the worst case might contain all cells of the grid, taking O(n*m) space. We also maintain the minCost array of size n*m.
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(0, 0)])
        minCost = [[float("inf")]*ncols for _ in range(nrows)]
        minCost[0][0] = 0
        while q:
            i, j = q.popleft()
            for d, (dx, dy) in enumerate(dirs):
                cost = 0 if grid[i][j]-1 == d else 1
                if i+dx in range(nrows) and j+dy in range(ncols) and minCost[i][j] + cost < minCost[i+dx][j+dy]:
                    minCost[i+dx][j+dy] = minCost[i][j] + cost
                    if not cost:
                        q.appendleft((i+dx, j+dy))
                    else:
                        q.append((i+dx, j+dy))
        return minCost[nrows-1][ncols-1]