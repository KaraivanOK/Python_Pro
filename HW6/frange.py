class Frange:
    def __init__(self, start, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop is None:
            if self.counter < self.start:
                self.counter += 1
                return self.counter - 1
            raise StopIteration
        else:
            if self.step is None:
                if self.start < self.stop:
                    self.start += 1
                    return self.start - 1
                raise StopIteration
            else:
                if self.step > 0:
                    if self.start < self.stop:
                        self.start += self.step
                        return self.start - self.step
                    raise StopIteration
                else:
                    if self.start > self.stop:
                        self.start += self.step
                        return self.start - self.step
                    raise StopIteration


frange = Frange
for i in frange(5):
    print(i)
print('-' * 20)
for i in frange(2, 5):
    print(i)
print('-' * 20)
for i in frange(2, 10, 2):
    print(i)
print('-' * 20)
for i in frange(10, 2, -2):
    print(i)
print('-' * 20)
for i in frange(2, 5.5, 1.5):
    print(i)
print('-' * 20)
for i in frange(11, 1, -2.5):
    print(i)
print('-' * 20)
for i in frange(1, 5):
    print(i)
print('-' * 20)
for i in frange(0, 5):
    print(i)
print('-' * 20)
for i in frange(0, 0):
    print(i)
print('-' * 20)
for i in frange(100, 0):
    print(i)
print('-' * 20)
assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(11, 1, -2.5)) == [11, 8.5, 6, 3.5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])
print('SUCCESS!')
