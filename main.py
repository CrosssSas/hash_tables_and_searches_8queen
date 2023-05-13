from random import *
import math


# Быстрая сортитровка
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


# Случайные входные данные
def generator(element_count, min_num, max_num):
    data = []
    for i in range(element_count):
        data.append(randint(min_num, max_num))

    return data


# Бинарный поиск
def bin_search(arr, the_desired_num):
    start_mark = 0
    end_mark = (len(arr) - 1)
    answer = []
    pivot = (start_mark + math.ceil(((end_mark - start_mark) + 1) / 2))
    while True:

        if arr[pivot] == the_desired_num:

            answer.append(pivot)

            if arr[pivot - 1] == arr[pivot]:
                x = 1
                while arr[pivot - x] == arr[pivot]:
                    answer.append(pivot - x)
                    x += 1

            if arr[pivot + 1] == arr[pivot]:
                x = 1
                while arr[pivot + x] == arr[pivot]:
                    answer.append(pivot + x)
                    x += 1

            break

        if start_mark == (end_mark - 1):
            if arr[start_mark] == the_desired_num:
                answer.append(arr[start_mark])
            elif arr[end_mark] == the_desired_num:
                answer.append(end_mark)

            break

        if arr[pivot] > the_desired_num:
            end_mark = pivot
            pivot = (start_mark + math.ceil((end_mark - start_mark) / 2))
            continue

        if arr[pivot] < the_desired_num:
            start_mark = pivot
            pivot = (start_mark + math.ceil((end_mark - start_mark) / 2))
            continue

    if not answer:
        print("Такого числа нет в списке")

    return quick(answer)


test_data = generator(200, 1, 100)
sorted_data = quick(test_data)
print(sorted_data)
final = bin_search(sorted_data, 87)
print("index:")
print(final)