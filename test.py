import random
key = "Саша"
key2 = "Сашаи"

hasher_buffer = list(key)
hasher = ""
for x in hasher_buffer:
    hasher += str(ord(x))

hasher_buffer2 = list(key2)
hasher2 = ""
for x in hasher_buffer2:
    hasher2 += str(ord(x))

randNum = random.randint(0, 100)
randNum2 = random.randint(0, 100)
index = (int(hasher) * randNum) % 10
a = int(hasher2) * randNum2
b = a % 10
index2 = (int(hasher2) * randNum2) % 11

print(index)
print(index2)
print(66768768760 % 10)