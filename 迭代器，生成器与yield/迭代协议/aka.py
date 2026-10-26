# 一次性使用
class apa:
    def __init__(self,max_a):
        self.max_a = max_a
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.max_a:
            self.a += 1
            return self.a-1
        else:
            raise StopIteration


# 若要多次

class bpb :
    def __init__(self,max_a):
        self.max_a = max_a

    def __iter__(self):
        return bpb_iterator(self.max_a)



class bpb_iterator:
    def __init__(self,max_a):
        self.max_a = max_a
        self.a = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.a < self.max_a:
            self.a += 1
            return self.a-1
        else:
            raise StopIteration