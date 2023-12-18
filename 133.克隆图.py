#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        # 使用哈希表记录被访问过的节点避免陷入死循环
        # key是原始图中的节点，value是克隆图对应的节点
        visited = {}
        # 将节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存入哈希表中
        visited[node] = Node(node.val, [])
        # 广度优先搜索
        while queue:
            # 取出队列头节点
            cur = queue.popleft()
            # 遍历该节点的邻居节点
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    # 如果没有访问过就克隆并存入哈希表
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[cur].neighbors.append(visited[neighbor])
        return visited[node]

# @lc code=end

