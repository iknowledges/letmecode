from collections import deque


def canFinish(numCourses, prerequisites):
    # 初始化入度
    indegrees = [0 for _ in range(numCourses)]
    # 初始化邻接表
    adjacency = [[] for _ in range(numCourses)]
    queue = deque()
    # 获取每门课程的入度和邻接表
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    # 将所有入度为0的课程放入队列
    for i in range(len(indegrees)):
        if not indegrees[i]:
            queue.append(i)
    # BFS TopSort
    while queue:
        pre = queue.popleft()
        numCourses -= 1
        for cur in adjacency[pre]:
            indegrees[cur] -= 1
            # 入度为0放入队列
            if not indegrees[cur]:
                queue.append(cur)
    # 拓扑排序出队次数等于课程个数，即numCourses==0，则课程安排成功
    return not numCourses


if __name__ == '__main__':
    # numCourses门课程，记为0到numCourses-1
    numCourses = 2
    # prerequisites[i]=[cur, pre]表示学习课程cur前必须先学习课程pre
    prerequisites = [[1,0],[0,1]]
    print(canFinish(numCourses, prerequisites))
