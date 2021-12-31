
"""
             --------------------       ACM八大输入输出格式之Python版         --------------------
                            https://blog.csdn.net/luovilonia/article/details/40860323
                                Python 输入的是野生字符串，所以要自己转换类型
"""

import sys

""" 
(1) 有多组输入数据，但是没有具体告诉你有多少组，只是让你对应每组输入，应该怎样输出。
"""

#     eg:

#     输入: 1 2 回车(显然，每次输入的数量是固定)
#     输出：3
#     ......

# 之后会继续让用户输入,每输入 “ 数字 空格 数字 回车 ”

while True:

    try:

        # 注意，在 python 3.x 中, raw_input() 和 input() 进行了整合，去除了raw_input(), 仅仅保留了 input() 函数，其接受任意
        # 性输入，将所有的输入默认为字符串进行处理，并返回字符串的类型。

        # eg:  a = input("input:")
        #      input: > ? 123    Out[3]: '123'
        #      这个提示框的意思就是让你输入这个东西

        a, b = map(int, input().strip().split())
        # (1) input() 函数接收到输入的原始字符串，
        # (2) strip([chars]) 方法用于移除字符串头尾指定的字符(默认为空格或者换行符)或者字符序列。
        # (3) split("") 方法用于将字符串按照()中的东西分割成 list_of_strings, 不指定的话默认是空格。

        print(a + b)

    # try - except 执行的过程: 1.先执行 try 代码块, 发现了错误, 主动中断现在的代码块;
    #                         2. 执行 except 代码块,如果 expect的
    #                         3. 程序向下执行;

    # EOFError 表示我们发现了一个不期望的文件尾，用来表示当前输入的结束
    except EOFError:

        break


# %%
""" 
(2) 1. 首先输入一个整数,告诉我们接下来有多少的数据
    2. 然后再输入每组数据的具体值
"""
# 首先: tcase 输入 int 类型的数据, 说明有多少组数据
tcase = int(input().strip())

# 其次: 按照 tcase 的值分别进行计算和输出
for case in range(tcase):
    a, b = map(int, input().strip().split())
    print(a + b)

# PS: 这个和之前一个的区别是，使用 for 循环可以在最后一组数据到达的时候结束。


# %%
"""
(3) 有多组数据，没有告诉你一共有多少组，但是明确告诉你当遇到什么的时候会结束；
"""
while True:
    a, b = map(int, input().strip().split())
    # 当输入遇到 0 的时候会跳出循环，输入结束
    if a == 0 or b == 0:
        break
    print(a + b)


# %%
"""
(4) 输入有多组数据，同时题目告诉了每组遇到什么的时候会结束，和(3)不同之处在于，每组都有相应的细化
"""
tcase = int(input().strip())
for case in range(tcase):
    a, b = map(int, input().strip().split())
    if a == 0 or b == 0:
        break
    print(a + b)


# %%
"""
(5) 1.首先输入一个整数，告诉一共有多少行；
    2.输入每一行，对于每一行的输入，划分为第一个数字和其他的输入，第一个数代表那一组数据一共有多少个输入
"""
tcase = int(input().strip())
for case in range(tcase):
    data = map(int, input().strip().split())
    n, array = data[0], data[1:]
    # 举一个例子，将每一行从第二个数字开始求和
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    print(sum)


# %%
"""
(6) 有多种输入数据，对于每组输入数据的第一个数代表该数据接下来要输入的数据量
"""
while True:
    try:
        data = map(int, input().strip().split())
        n, array1 = data[0], data[1:]
        sum = 0
        for i in range(len(array1)):
            sum += array1[i]
            print(sum)

    except EOFError:
        # 区分程序异常和程序执行错误
        raise


# %%
"""
(7) 在每组输出的时候添加一个换行
"""
while True:
    try:
        a, b = map(int, input().strip().split())
        print(a + b)
    except EOFError:
        break


# %%

"""
这种类型的输出注意的就是换行，这类题目说在输出样例中，每组样例之间有什么什么，所以我们在对应输出的同时要判断一下是否是最后一组输
出，如果不是，就将题目所说的东西输出（一般是换行或空格），如果是，就直接结束。
"""

while True:

    data = raw_input().strip()

    # 如果 data 字符串之中存在空格字符，那么输出True, 否则输出False
    if data.isspace():
        break
    else:
        data = map(int, data)
        n, array = data[0], data[1:]

        sum = 0
        for i in range(n):
            sum += array[i]
        print(sum)

        
