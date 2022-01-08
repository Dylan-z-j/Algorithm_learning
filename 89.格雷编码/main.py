"""
设 nn 阶格雷码集合为 G(n)G(n)，则 G(n+1)G(n+1) 阶格雷码为：
给 G(n)G(n) 阶格雷码每个元素二进制形式前面添加 00，得到 G'(n)G 
′
 (n)；
设 G(n)G(n) 集合倒序（镜像）为 R(n)R(n)，给 R(n)R(n) 每个元素二进制形式前面添加 11，得到 R'(n)R 
′
 (n)；
G(n+1) = G'(n) ∪ R'(n)G(n+1)=G 
′
 (n)∪R 
′
 (n) 拼接两个集合即可得到下一阶格雷码。

作者：jyd
链接：https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
  
    def grayCode(self, n: int) -> List[int]:
        
        if n == 1:
            
            bin_lis = ['0', '1']
            res = []
            
            for i in range(len(bin_lis)):
            
              res.append(int(bin_lis[i], 2))
              
            return res
        
        else:
            bin_lis = ['0', '1']
            
            for i in range(n - 1):
                left = ['0' + bin_lis[j] for j in range(len(bin_lis))]
                bin_lis.reverse()
                right = ['1' + bin_lis[j] for j in range(len(bin_lis))]
                bin_lis = left + right
            
            res = []
            
            for i in range(len(bin_lis)):
                res.append(int(bin_lis[i], 2))
            
            return res
