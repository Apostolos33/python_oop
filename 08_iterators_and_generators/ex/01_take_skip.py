class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < self.count:
            return self.idx * self.step
        raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

