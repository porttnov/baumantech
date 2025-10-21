from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    if not triangle or not triangle[0]:
        return 0
    
    dp = triangle[-1][:]
    
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
    
    return dp[0]

# example
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
triangle2 = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]

print(minimum_total(triangle1))  # 11
print(minimum_total(triangle2))  # 0
