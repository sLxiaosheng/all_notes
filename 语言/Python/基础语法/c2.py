
# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

# 初始化 A 和 B 的元素数量分别为 m 和 n。

class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        i = j = 0
        while i < n:
            print(i)
            A.pop()
            i += 1
        while j < n:
            print(j)
            con = B[j]
            A.append(con)
            j += 1
        print(self.sorting(A))

    def sorting(self,listness):
        for i in range(0,len(listness)):
            for j in range(0,len(listness)):
                if listness[i] < listness[j]:
                    listness[i], listness[j] = listness[j], listness[i]
        return listness


A = input('A列表：')
m = int(input('A列表有多少个值'))
B = (input('B列表：'))
n = int(input('B列表有多少个值'))
Solution1 = Solution()
Solution1.merge(A,m ,B ,n )