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


class InterSearch:

    def __init__(self):
        self.left = None
        self.right = None
        self.K = None
        self.answer = None
        self.sequence = []
        self.i = None

    def initialization(self, K, sequence):
        self.sequence = sequence
        self.K = K
        self.left = 0
        self.right = (len(sequence)-1)

    def find_element_main_function(self):

        self.i = (((self.K - self.sequence[self.left]) * (self.left - self.right)) // (
                    self.sequence[self.left] - self.sequence[self.right])) + self.left

        if self.sequence[self.i] == self.K:
            self.answer = self.i
        elif self.sequence[self.i] > self.K:

            if self.right == (self.i - 1):
                self.answer = "Значение не существует"
            else:
                self.right = (self.i - 1)
                self.find_element_main_function()

            self.find_element_main_function()
        elif self.sequence[self.i] < self.K:

            if self.left == (self.i + 1):
                self.answer = "Значение не существует"
            else:
                self.left = (self.i + 1)
                self.find_element_main_function()

        return self.answer

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


Inter = InterSearch()
# SEQQQ = [-2, 0, 3, 5, 7, 9, 11, 15, 18]
SEQU = quick(generator(200, 1, 100))

Inter.initialization(8, SEQU)

Gubanov = Inter.find_element_main_function()


print(SEQU)
print(Gubanov)
print(Inter.duplicate_search(Gubanov))
