def lis(arr):
    n = len(arr)
    if n == 0:
        return 0, []

    # Массив для хранения длин LCS для каждого элемента
    dp = [1] * n
    # Массив для восстановления последовательности
    prev = [-1] * n

    # Заполнение dp массива
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Длина наибольшей возрастающей подпоследовательности
    lis_length = max(dp)

    # Восстановление самой последовательности
    index = dp.index(lis_length)
    lis_sequence = []
    while index != -1:
        lis_sequence.append(arr[index])
        index = prev[index]

    lis_sequence.reverse()  # Переворачиваем, так как восстанавливали последовательность с конца

    return lis_length, lis_sequence


# Пример использования
arr = [3, 10, 2, 1, 20]
length, sequence = lis(arr)

print(f"Длина наибольшей возрастающей подпоследовательности: {length}")
print(f"Наибольшая возрастающая подпоследовательность: {sequence}")
