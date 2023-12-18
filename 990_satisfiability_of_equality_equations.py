class UnionFind:
    def __init__(self):
        # parent存储每个变量的连通分量信息，
        # 其中的每个元素表示当前变量所在的连通分量的父节点信息，
        # 如果父节点是自身，说明该变量为所在的连通分量的根节点
        self.parent = list(range(26))
    
    # 查找操作：沿着当前变量的父节点一路向上查找，直到找到根节点。
    def find(self, index):
        if index == self.parent[index]:
            return index
        # 路径压缩 
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]
    
    # 合并操作：将第一个变量的根节点的父节点指向第二个变量的根节点
    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)


def equationsPossible(equations):
    """
    :type equations: List[str]
    :rtype: bool
    """
    uf = UnionFind()
    # 首先遍历所有的等式，构造并查集。
    # 同一个等式中的两个变量属于同一个连通分量，因此将两个变量进行合并。
    for st in equations:
        if st[1] == "=":
            index1 = ord(st[0]) - ord("a")
            index2 = ord(st[3]) - ord("a")
            uf.union(index1, index2)
    # 然后遍历所有的不等式。同一个不等式中的两个变量不能属于同一个连通分量，
    # 因此对两个变量分别查找其所在的连通分量，如果两个变量在同一个连通分量中，则返回false。 
    for st in equations:
        if st[1] == "!":
            index1 = ord(st[0]) - ord("a")
            index2 = ord(st[3]) - ord("a")
            if uf.find(index1) == uf.find(index2):
                return False
    return True


if __name__ == '__main__':
    print(equationsPossible(["a==b","b!=a"]))
