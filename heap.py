import heapq

def calculate_total_time(n, m, times):
    # Инициализируем min-heap первыми m клиентами
    heap = times[:m]
    heapq.heapify(heap)

    # Обрабатываем остальных клиентов
    for time in times[m:]:
        # Касса освобождается (удаляем минимальный элемент)
        min_time = heapq.heappop(heap)
        # Добавляем нового клиента на освободившуюся кассу
        heapq.heappush(heap, min_time + time)

    # Максимальное время в куче — общее время обработки
    return max(heap)

# Ввод
n, m = map(int, input().split())
times = list(map(int, input().split()))

# Вывод
print(calculate_total_time(n, m, times))
