from random import *


def generator(element_count, min_num, max_num):
    data = []
    for i in range(element_count):
        data.append(randint(min_num, max_num))

    return data


def quick(firstArray):
    less = []
    equal = []
    greater = []

    if len(firstArray) > 1:
        pivot = firstArray[0]
        for i in firstArray:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        return quick(less) + equal + quick(greater)
    else:
        return firstArray


def get_fib_index_or_value(value, flag):
    index = 2
    fibo_buffer = [0, 1, None]
    while True:
        fibo_buffer[2] = fibo_buffer[0] + fibo_buffer[1]
        index += 1

        if flag:
            if index == value:
                return fibo_buffer[2]
        else:
            if fibo_buffer[2] >= value:
                return index

        fibo_buffer[0] = fibo_buffer[1]
        fibo_buffer[1] = fibo_buffer[2]


class FiboSearch:
    def __init__(self):
        self.answer = None
        self.p = None
        self.q = None
        self.i = None
        self.K = None
        self.sequence = []

    def start_initialization(self, sequence, K):
        k = (get_fib_index_or_value(len(sequence) + 1, False) - 1)
        M = (get_fib_index_or_value((k + 1), True) - (len(sequence) + 1))
        self.i = (get_fib_index_or_value(k, True) - M)
        self.p = get_fib_index_or_value((k - 1), True)
        self.q = get_fib_index_or_value((k - 2), True)
        self.sequence = sequence
        self.K = K

    def find_value_start_point(self):
        if self.i < 0:
            buff = self.check_p()
            if buff == -1:
                self.answer = -1
        elif self.i >= len(self.sequence):
            buff = self.check_q()
            if buff == -1:
                self.answer = -1

        if self.K < self.sequence[self.i]:
            buff = self.check_q()
            if buff == -1:
                self.answer = -1
        elif self.K > self.sequence[self.i]:
            buff = self.check_p()
            if buff == -1:
                self.answer = -1
        elif self.K == self.sequence[self.i]:
            self.answer = self.i

        if self.answer == -1:
            return "Значение не существует"
        else:
            return self.answer

    def check_q(self):
        if self.q == 0:
            return -1
        else:
            self.i -= self.q
            self.p, self.q = self.q, (self.p - self.q)
            self.find_value_start_point()

    def check_p(self):
        if self.p == 1:
            return -1
        else:
            self.i += self.q
            self.p -= self.q
            self.q -= self.p
            self.find_value_start_point()

    def duplicate_search(self, index):

        duplicates = [index]

        if self.sequence[index - 1] == self.sequence[index]:
            x = 1
            while self.sequence[index - x] == self.sequence[index]:
                duplicates.append(index - x)
                x += 1

        if self.sequence[index + 1] == self.sequence[index]:
            x = 1
            while self.sequence[index + x] == self.sequence[index]:
                duplicates.append(index + x)
                x += 1

        return quick(duplicates)


F = FiboSearch()

# SEQ = [-2, 0, 3, 5, 7, 9, 11, 15, 18, 21]
SEQ = generator(200, 1, 100)
SEQQ = quick(SEQ)
print(SEQQ)

F.start_initialization(SEQQ, 2)

answer = F.find_value_start_point()

duplicat = F.duplicate_search(answer)

print("Индекс:")
print(duplicat)
