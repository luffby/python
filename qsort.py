import random

def quicksort(arr):
    # Вызов вспомогательной функции с начальным диапазоном
    return quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, low, high):
    if low < high:
        # Разделяем массив и получаем индекс опорного элемента
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем две части массива
        quicksort_helper(arr, low, pivot_index - 1)
        quicksort_helper(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    # Случайный выбор индекса опорного элемента
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]

    # Перемещаем опорный элемент в конец массива
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Стандартное разделение массива вокруг опорного элемента
    i = low - 1  # Индекс для элементов меньших опорного
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы

    # Перемещаем опорный элемент на его окончательное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Возвращаем индекс опорного элемента


# Пример использования:
arr = [10, 7, 8, 9, 1, 5,6,7,4,7,9,5,3,6,8,9,4,6,8,4]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Вывод: [1, 5, 7, 8, 9, 10]
