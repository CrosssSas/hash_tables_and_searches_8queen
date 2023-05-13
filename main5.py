class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.elementCount = 0
        self.chainPeaces = [None] * self.size

    def hash_fun(self, key):
        hasher_buffer = list(key)
        hasher = ""
        for x in hasher_buffer:
            hasher += str(ord(x))
        index = int(hasher) % self.size
        return index

    def adder(self, key, value):
        if self.get_value(key) is not None:
            print("Значение уже существует")
            return
        index = self.hash_fun(key)
        node = Node(key, value)
        if self.chainPeaces[index] is None:
            self.chainPeaces[index] = node
            self.elementCount += 1
            print("Успешно добавлено (цепочки)")
        else:
            print("Вознкла коллизия (цепочки)")
            if str(type(self.chainPeaces[index])) == "<class 'list'>":
                self.chainPeaces[index].append(node)
                self.elementCount += 1
                print("Успешно разрешено (цепочки)")
            else:
                arr = [self.chainPeaces[index]]
                self.chainPeaces[index] = arr
                self.chainPeaces[index].append(node)
                self.elementCount += 1
                print("Успешно разрешено (цепочки)")

        if (self.size * 0.7) <= self.elementCount:
            self.resizer()

    def get_value(self, key):
        index = self.hash_fun(key)
        if str(type(self.chainPeaces[index])) == "<class 'list'>":
            for i in range(len(self.chainPeaces[index])):
                if self.chainPeaces[index][i].key == key:
                    return self.chainPeaces[index][i].value

            return None

        else:
            try:
                if self.chainPeaces[index].key == key:
                    return self.chainPeaces[index].value
                else:
                    return None
            except AttributeError:
                return None

    def remover(self, key):
        index = self.hash_fun(key)
        if str(type(self.chainPeaces[index])) == "<class 'list'>":
            for i in range(len(self.chainPeaces[index])):
                if self.chainPeaces[index][i].key == key:

                    self.chainPeaces[index].pop(i)

                    if len(self.chainPeaces[index]) == 1:
                        self.chainPeaces[index] = self.chainPeaces[index][0]
                    elif len(self.chainPeaces[index]) == 0:
                        self.chainPeaces[index] = None

                    self.elementCount -= 1
                    print("Успешно удаленно (цепочки)")
                    return

            return "Значение не существует"

        else:
            try:
                if self.chainPeaces[index].key == key:
                    self.chainPeaces[index] = None
                    self.elementCount -= 1
                    print("Успешно удаленно (цепочки)")
                else:
                    return "Значение не существует"
            except AttributeError:
                return "Значение не существует"

    def resizer(self):

        buff_table = self.chainPeaces
        self.size = self.size*2
        self.chainPeaces = [None] * self.size
        self.elementCount = 0

        for i in range(len(buff_table)):
            if str(type(buff_table[i])) == "<class 'list'>":
                for j in range(len(buff_table[i])):
                    old_key = buff_table[i][j].key
                    old_value = buff_table[i][j].value
                    self.adder(old_key, old_value)
            else:
                try:
                    old_key = buff_table[i].key
                    old_value = buff_table[i].value
                    self.adder(old_key, old_value)
                except AttributeError:
                    continue

        print("Произведено рехэширование (цепочки)")

    def clear(self):
        for i in range(len(self.chainPeaces)):
            self.chainPeaces[i] = None


# table = HashTable(10)
# table.adder("Катя", "88005553535")
# table.adder("Коля", "2281337")
# table.adder("Зинаида", "1111111111")
# table.clear()
# print(table.get_value("Зинаида"))
# table.adder("Карина", "222222222")
# table.adder("Женя", "333333333333")
# table.adder("Абоба", "444444444444")
# table.adder("Реп", "66666666666")
