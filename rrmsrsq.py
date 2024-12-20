import math


class RSQ:
    def __init__(self, arr):
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n))
        self.blocks = [0] * ((self.n + self.block_size - 1) // self.block_size)

        # Заполнение блоков суммами
        for i in range(self.n):
            self.blocks[i // self.block_size] += arr[i]

        self.arr = arr

    def query(self, l, r):
        sum_val = 0

        # Индексы блоков
        block_left = l // self.block_size
        block_right = r // self.block_size

        if block_left == block_right:
            # Если запрос в одном блоке
            for i in range(l, r + 1):
                sum_val += self.arr[i]
        else:
            # Левый блок (от l до конца блока)
            end_of_left_block = (block_left + 1) * self.block_size - 1
            for i in range(l, min(r + 1, end_of_left_block + 1)):
                sum_val += self.arr[i]

            # Все полные блоки между левой и правой границей
            for block in range(block_left + 1, block_right):
                sum_val += self.blocks[block]

            # Правый блок (с начала до r)
            start_of_right_block = block_right * self.block_size
            for i in range(start_of_right_block, r + 1):
                sum_val += self.arr[i]

        return sum_val


# Пример использования:
arr = [1, 3, 2, 7, 9, 5, 4, 6, 8, 10]
rsq = RSQ(arr)

# Запрос: сумма в диапазоне [2, 8]
print(rsq.query(2, 8))  # Ответ: 33

import math


class RMQ:
    def __init__(self, arr):
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n))
        self.blocks = [float('inf')] * ((self.n + self.block_size - 1) // self.block_size)

        # Заполнение блоков минимальными значениями
        for i in range(self.n):
            self.blocks[i // self.block_size] = min(self.blocks[i // self.block_size], arr[i])

        self.arr = arr

    def query(self, l, r):
        min_val = float('inf')

        # Индексы блоков
        block_left = l // self.block_size
        block_right = r // self.block_size

        if block_left == block_right:
            # Если запрос в одном блоке
            for i in range(l, r + 1):
                min_val = min(min_val, self.arr[i])
        else:
            # Левый блок (от l до конца блока)
            end_of_left_block = (block_left + 1) * self.block_size - 1
            for i in range(l, min(r + 1, end_of_left_block + 1)):
                min_val = min(min_val, self.arr[i])

            # Все полные блоки между левой и правой границей
            for block in range(block_left + 1, block_right):
                min_val = min(min_val, self.blocks[block])

            # Правый блок (с начала до r)
            start_of_right_block = block_right * self.block_size
            for i in range(start_of_right_block, r + 1):
                min_val = min(min_val, self.arr[i])

        return min_val


# Пример использования:
arr = [1, 3, 2, 7, 9, 5, 4, 6, 8, 10]
rmq = RMQ(arr)

# Запрос: минимум в диапазоне [2, 8]
print(rmq.query(2, 8))  # Ответ: 2
