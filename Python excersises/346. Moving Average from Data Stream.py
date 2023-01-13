from collections import deque

# Solution 1
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


# Solution 2 - work in progress

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.qeue = deque

    def next(self, val: int) -> float:
        if not deque:
            self.qeue.append(val)

        if len(self.qeue) == self.size:
            first_element = self.qeue[0]
            self.qeue.remove(first_element)
        # add

        ans = sum(self.qeue) / len(self.qeue)

        return ans


movingAverage = MovingAverage(3);
movingAverage.next(1)
movingAverage.next(10)
movingAverage.next(3)
print(movingAverage.next(5))