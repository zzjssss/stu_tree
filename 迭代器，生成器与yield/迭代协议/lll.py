

#创建迭代器
# 从a到零
class aaa:
    def __init__(self,a):
        self.a = a
    def __iter__(self):
        return self
    def __next__(self):
        if self.a > 0:
            self.a -= 1
            return self.a
        else:
            raise StopIteration

#迭代工厂
class aaabbb:
    def __init__(self,a):
        self.a = a
    def __iter__(self):
        return aaa(self.a)

if  __name__ == '__main__':
    b = aaa(5)
    for i in b:
        print(i)