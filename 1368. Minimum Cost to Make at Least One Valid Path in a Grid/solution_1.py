"""
This approach uses dynamic programming with iterative refinement to find the minimum cost to create at least one valid path in the grid.

An iteration "n" finds the optimal paths that require atmost "n" changes. The process continues until no further improvements can be made, indicating convergence to the optimal solution.

Let n be the number of rows and m be the number of columns in the grid.

Time Complexity: O((n*m)^2)

The algorithm has an outer loop that continues until convergence, where k is the number of iterations needed. In each iteration, we perform a forward pass and a backward pass through the entire grid, each taking O(n*m) time. Therefore, the total time complexity is O(n*m*k).

The value of k depends on the grid configuration and in the worst case could be proportional to n*m, making the worst-case time complexity O((n*m)^2).

Space Complexity: O(n*m)

The algorithm uses two 2D arrays - minChanges and prevState, each of size n*m.
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        minChange = [[float('inf')]*ncols for _ in range(nrows)]
        minChange[0][0] = 0
        while True:
            # Store previous state to check for convergence
            prevState = [row[:] for row in minChange]

            # Forward pass: check cells coming from left and top
            for i in range(nrows):
                for j in range(ncols):
                    # Check cell above
                    if i-1>=0:
                        minChange[i][j] = min(minChange[i][j], minChange[i-1][j] + (0 if grid[i-1][j] == 3 else 1))

                    # Check cell to the left
                    if j-1>=0:
                        minChange[i][j] = min(minChange[i][j], minChange[i][j-1] + (0 if grid[i][j-1] == 1 else 1))
            
            # Backward pass: check cells coming from below and the right
            for i in range(nrows-1, -1, -1):
                for j in range(ncols-1, -1, -1):
                    # Check cell below
                    if i+1<nrows:
                        minChange[i][j] = min(minChange[i][j], minChange[i+1][j] + (0 if grid[i+1][j] == 4 else 1))

                    # Check cell to the left
                    if j+1<ncols:
                        minChange[i][j] = min(minChange[i][j], minChange[i][j+1] + (0 if grid[i][j+1] == 2 else 1))
            
            # If no changes were made in this iteration, we've found optimal solution
            if minChange == prevState:
                break
        return minChange[nrows-1][ncols-1]