class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []
        self.count = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        if len(self.stream) > self.k:
            if self.stream[-self.k - 1] == self.value:
                self.count -= 1
        return self.count == self.k
