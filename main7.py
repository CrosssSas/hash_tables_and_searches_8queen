import random


class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key


class StandardHashTable:
    def __init__(self, size):
        self.size = size
        self.elementCount = 0
        self.storage = [None] * self.size
        self.hashNum = 0

    def hash_fun_standard(self, key):
        if self.elementCount == 0:
            self.hashNum = random.randint(1, self.size)
        hasher_buffer = list(key)
        hasher = 0
        for x in hasher_buffer:
            hasher += ord(x)
        index = (hasher // self.hashNum) % self.size
        return index

    def adder(self, key, value):
        index = self.hash_fun_standard(key)
        node = Node(key, value)
        if self.storage[index] is None:
            self.storage[index] = node
            self.elementCount += 1
            print("Успешно добавлено")
            if self.size * 0.5 <= self.elementCount:
                self.resize_rehash(False)
        else:
            print("Вознкла коллизия")
            self.resize_rehash(True)
            self.adder(key, value)
            print("Успешно разрешенно")

    def get_value(self, key):
        index = self.hash_fun_standard(key)
        try:
            return self.storage[index].value
        except AttributeError:
            print("Значение не существует")

    def resize_rehash(self, flag):
        buff_store = self.storage
        if not flag:
            self.size *= 2
        self.storage = [None] * self.size
        self.elementCount = 0

        for i in range(len(buff_store)):
            if buff_store[i] is not None:
                old_key = buff_store[i].key
                old_value = buff_store[i].value
                self.adder(old_key, old_value)
        print("Рехэширование")

    def remover(self, key):
        index = self.hash_fun_standard(key)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None
                print("Успешно удаленно")
            else:
                print("Такого ключа не существет")
        else:
            print("Такого ключа не существет")


table = StandardHashTable(10)
table.adder("Ваня", "346456")
table.adder("Саша", "8803332605")
table.adder("Коля", "475837645")
table.adder("Надя", "752833704")
table.adder("Женя", "995837")
print(table.get_value("Ваня"))
print(table.get_value("Саша"))
print(table.get_value("Коля"))
print(table.get_value("Надя"))
print(table.get_value("Женя"))
table.remover("Надя")
print(table.get_value("Женя"))