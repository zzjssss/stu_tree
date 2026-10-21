
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