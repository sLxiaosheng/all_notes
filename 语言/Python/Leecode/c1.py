
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 网格的长，宽
        m, n = len(grid), len(grid[0])
        # 网格每一个坐标的访问状态
        visit = [[False] * n for y in range(m)]
        # 找出最开始时，网格中所有坏橘子的坐标
        stack = [[y,x] for y in range(m) for x in range(n) if grid[y][x]==2]
        # 坏橘子传染好橘子的四个方向，上下左右
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        # 初始时间
        minute = 0
        
        # 开始坏橘子传染好橘子的循环，直到没有好橘子可以被传染
        while True:
            # 初始化一个stack_next，把这一轮变坏的橘子装进里面
            stack_next = []
            # 开始对坏橘子进行审查，主要是看上下左右有没有好橘子
            while stack:
                # 拿出坏橘子的坐标点
                y, x = stack.pop()
                # 再看坏橘子上下左右的坐标对应的坐标
                for d in direction:
                    y_new, x_new = y + d[0], x + d[1]
                    # 如果坐标在网格范围内，而且坐标没有被访问过，且这个坐标确实有个好橘子
                    if -1 < y_new < m and -1 < x_new < n and not visit[y_new][x_new] and grid[y_new][x_new] == 1:
                        # 观察慰问一下这个好橘子，表示已经访问过了
                        visit[y_new][x_new] = True
                        # 告诉这个好橘子，你已被隔壁的坏橘子感染，现在你也是坏橘子了
                        grid[y_new][x_new] = 2
                        # 放进stack_next里面，集中管理，精准隔离，方便排查下一轮会变坏的橘子
                        stack_next.append([y_new, x_new])
            # 如果橘子们都检查完了发现再无其他坏橘子，终止循环，宣布疫情结束
            if not stack_next: break
            # 把这一轮感染的坏橘子放进stack里，因为我们每一轮都是从stack开始搜索的
            stack = stack_next
            # 看来橘子们还没凉透，来，给橘子们续一秒，哦不，续一分钟
            minute += 1
        
        # 经过传染，审查，隔离的循环后，如果还有好橘子幸存，返回-1宣布胜利，否则返回橘子们的存活时间
        return -1 if ['survive' for y in range(m) for x in range(n) if grid[y][x]==1] else minute

# 作者：quantumdriver
# 链接：https://leetcode-cn.com/problems/rotting-oranges/solution/python-bfs-jie-fa-dai-ma-fu-xiang-xi-jie-shi-by-qu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# minute = 0
# inf = False
# class Solution(object):
#     def orangesRotting(self, grid):
#         i = j = 0
#         for i in range(0, len(grid)):
#             for j in range(0,len(grid[i])):
#                 if int(grid[i][j]) == 2:
#                     print(3)
#                     inf = True
#                     global minute
#                     minute = rotting(grid,i,j)
#                     minute = result(minute)
#         print(minute)
    
#     def rotting(self,grid,i,j):
#         if grid[i][j+1] & grid==1:
#             grid[i][j+1] = 2
#         if grid[i][j-1] & grid==1:
#             grid[i][j-1] = 2
#         if grid[i+1][j] & grid==1:
#             grid[i+1][j] = 2
#         if grid[i-1][j] & grid==1:
#             grid[i-1][j] = 2
#         minute += 1
#         print("`")
#         print(minute)
#         return minute
    
#     def result(self,minute):
#         if minute == 0 & inf:
#             return -1
#         return minute

# orange = list(input())
# print(orange)
# orange1 = Solution()
# orange = orange1.orangesRotting(orange)
# print(orange)

        
        


        
