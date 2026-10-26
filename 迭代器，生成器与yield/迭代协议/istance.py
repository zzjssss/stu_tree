# 举例迭代对象
class CountdownIterator:
    def __init__(self, start):
        self.current = start  # 接收传入的start，保存当前值

    # 迭代器必须实现 __iter__
    def __iter__(self):
        return self

    # 迭代器必须实现 __next__
    def __next__(self):
        if self.current < 0:
            raise StopIteration  # 迭代结束标记
        val = self.current
        self.current -= 1
        return val

class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return CountdownIterator(self.start) # 每次全新迭代器
            # CountdownIterator是一个迭代器
"""    


"""
#这些是迭代器
class Fib:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b  # 更新两个计数器
        return fib


f = Fib(1000)
for i in f:
    print(i, end=' ')

# 迭代器例子
class Countdown:                     # 手写一个迭代器
    def __init__(self, n): self.n = n
    def __iter__(self): return self          # 返回迭代器本身
    def __next__(self):
        if self.n <= 0: raise StopIteration  # 终止信号
        self.n -= 1
        return self.n + 1