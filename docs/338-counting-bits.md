## 题目：
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

**示例**：

- 输入：n = 5
- 输出：[0,1,1,2,1,2]
- 解释：

0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

## 题解：
| 整数 | 二进制 | 比特位数 |
| --- | --- | --- |
| 0 | 000 | 0 |
| 1 | 001 | 1 |
| 2 | 010 | 1 |
| 3 | 011 | 2 |
| 4 | 100 | 1 |
| 5 | 101 | 2 |
| 6 | 110 | 2 |
| 7 | 111 | 3 |

动态规划思路：当计算i的比特数时，如果存在$0\leq j<i$且i的二进制表示只比j多一个1，则可以快速得到i的比特数，$bits[i]=bits[j]+1$
##### 方法一 —— 最高有效位
对于正整数x，如果已知最大的正整数y，使得$y\leq x$且y是2的整数次幂，则y的二进制表示中只有最高位是1，其余都是0，此时称y为x的最高有效位。令z=x-y，则有$bits[x]=bits[z]+1$。
求解步骤：

1. 初始化最高有效位数highBit=0，遍历从1到n的每个正整数i；
2. 判断i是否是2的整数次幂，如果是，即$i\&(i-1)=0$，则更新最高有效位数highBit=i，否则不做处理；
3. 每次遍历都更新$bits[i]=bits[i-highBit]+1$，最后返回bits。
```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> bits(n + 1);
        int highBit = 0;
        for (int i = 1; i <= n; i++) {
            if ((i & (i - 1)) == 0) {
                highBit = i;
            }
            bits[i] = bits[i - highBit] + 1;
        }
        return bits;
    }
};
```
##### 方法二 —— 最低有效位
对于正整数x，对其向下取整表示为$\lfloor x\rfloor$。设数组为bits，如果$bits[\lfloor\frac{x}{2}\rfloor]$的值已知，则可以得到$bits[x]$的值：

- 如果x是偶数，则$bits[x]=bits[\lfloor\frac{x}{2}\rfloor]$；
- 如果x是奇数，则$bits[x]=bits[\lfloor\frac{x}{2}\rfloor]+1$。

上述两种情况可以合并为：$bits[x]$等于$bits[\lfloor\frac{x}{2}\rfloor]$的值加上$x$除以2的余数，而$\lfloor\frac{x}{2}\rfloor$可由$x>>1$得到，$x$除以2的余数可以由$x \& 1$得到，因此有：$bits[x]=bits[x>>1]+(x\&1)$。
由于二进制右移一位，等价于将其二进制表示的最低位去掉，所有这个方法称为最低有效位。
```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> bits(n + 1);
        for (int i = 1; i <= n; i++) {
            bits[i] = bits[i >> 1] + (i & 1);
        }
        return bits;
    }
};
```
