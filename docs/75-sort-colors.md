## 题目：
给定一个包含红色、白色和蓝色、共 n_ _个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

**示例**：

- 输入：nums = [2,0,2,1,1,0]
- 输出：[0,0,1,1,2,2]

## 题解：

1. 初始化三个指针：0指针、2指针和移动指针，移动指针从前到后遍历，判断指向的这个点是不是0或者2，如果不是则继续移动；
2. 如果是0，则与0指针的元素交换，0指针后移；
3. 如果是2，则与2指针的元素交换，2指针前移；注意：这一步时移动指针不能后移，否则输入[1,2,0]会出bug。
4. 移动指针的位置超过了2指针，结束。

```cpp
class Solution {
public:
void sortColors(vector<int>& nums) {
    int i = 0;
    int j = nums.size() - 1;
    int idx = 0;
    while (idx <= j) {
        if (nums[idx] == 0) {
            int tmp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = tmp;
            ++i;
            ++idx;
        } else if (nums[idx] == 2) {
            int tmp = nums[j];
            nums[j] = nums[idx];
            nums[idx] = tmp;
            --j;
        } else {
            ++idx;
        }
    }
}
};
```
