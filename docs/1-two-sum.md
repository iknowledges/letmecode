1. 创建一个map；
2. for循环遍历nums数组；
3. 用target减nums[i]，以计算哪个数能跟当前数相加得到target；
4. 检查map里有没有这个数，如果有则返回结果，如果没有则把{num[i]: i}放入map中。
