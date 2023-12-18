#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 子节点是26个字母，每一个下标代表一个字母
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            # 计算字母对应下标位置
            ch = ord(ch) - ord("a")
            # 子节点不存在就在对应位置创建新的子节点
            if not node.children[ch]:
                node.children[ch] = Trie()
            # 沿指针移动子节点
            node = node.children[ch]
        node.isEnd = True


    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.searchPrefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

