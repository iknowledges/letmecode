## 题目：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

**示例**：

- 输入：s = "()[]{}"
- 输出：true

## 题解：

1. 初始化哈希表存储括号对应关系(右括号: 左括号)，然后遍历字符串，判断字符是否存在于哈希表的key值。
2. 如果字符不存在，说明是左括号，则入栈。
3. 如果字符存在，说明是右括号，判断对应左括号是否是栈顶元素，如果不相同直接返回false，否则出栈。
4. 如果字符不在哈希表中，并且栈为空，返回false。
5. 循环结束判断栈是否为空，如果为空则返回true，否则返回false。

```cpp
class Solution {
public:
bool isValid(string s) {
    if (s.size() % 2 == 1)
        return false;

    unordered_map<char,char> map = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    };
    
        stack<char> stk;
    
        for (char c : s) {
            if (map.count(c) == 0) {
                stk.push(c);
            } else {
                if (stk.empty() || map[c] != stk.top()) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.empty();
    }
};
```
