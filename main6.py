import random
import main5


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class TableRandomHash:
    def __init__(self, size):
        self.size = size
        self.elementCount = 0
        self.storage = [None]*self.size
        self.randNumStorage = main5.HashTable(10)

    def hash_rand_fun(self, key, flag):

        hasher_buffer = list(key)
        hasher = ""
        for x in hasher_buffer:
            hasher += str(ord(x))

        if flag:
            randNum = random.randint(0, (self.size + (13768437 - self.size)))
            self.randNumStorage.adder(key, randNum)
            index = (int(hasher) // randNum) % (self.size + 1)
            if index == self.size:
                index -= 1
            return index
        else:
            try:
                index = (int(hasher) // self.randNumStorage.get_value(key)) % (self.size + 1)
                if index == self.size:
                    index -= 1
                return index
            except TypeError:
                print("Значение не существует")
                return None

    def adder(self, key, value):
        index = self.hash_rand_fun(key, True)
        node = Node(key, value)
        if self.storage[index] is None:
            self.storage[index] = node
            self.elementCount += 1
            print("Успешно добавлено")
            if self.size * 0.5 <= self.elementCount:
                self.resizer()
        else:
            print("Вознкла коллизия")
            self.randNumStorage.remover(key)
            self.adder(key, value)
            print("Успешно разрешенно")

    def get_value(self, key):
        index = self.hash_rand_fun(key, False)
        try:
            return self.storage[index].value
        except TypeError:
            return None

    def remover(self, key):
        index = self.hash_rand_fun(key, False)
        try:
            if self.storage[index] is not None:
                if self.storage[index].key == key:
                    self.storage[index] = None
                    print("Успешно удаленно")
                else:
                    print("Такого ключа не существет")
            else:
                print("Такого ключа не существет")
        except TypeError:
            print("Такого ключа не существует")

    def resizer(self):
        buff_store = self.storage
        self.size = self.size * 2
        self.storage = [None] * self.size
        self.elementCount = 0

        self.randNumStorage.clear()
        for i in range(len(buff_store)):
            if buff_store[i] is not None:
                old_key = buff_store[i].key
                old_value = buff_store[i].value
                self.adder(old_key, old_value)

        print("Произведено рехэширование")


rand = TableRandomHash(10)
rand.adder("Саша", "8803332605")
rand.adder("Коля", "475837645")
rand.adder("Надя", "752833704")
rand.adder("Иван", "8803332605")
rand.adder("Даня", "475837645")
rand.adder("Дима", "752833704")
rand.remover("Надя")
print(rand.get_value("Саша"))
print(rand.get_value("Дима"))
