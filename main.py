# Метод минимальных тарифов для решения транспортной задачи

def print_matrix(matrix, row_labels, col_labels):
    """Вывод матрицы в удобочитаемом виде."""
    print("     " + "  ".join([f"{c:>3}" for c in col_labels]))
    for i, row in enumerate(matrix):
        print(f"{row_labels[i]:>3} | " + "  ".join([f"{v:>3}" if v is not None else "  -" for v in row]))
    print()

def min_tariff_method(supply, demand, cost):
    """
    Реализация метода минимальных тарифов.
    :param supply: Список объемов поставок.
    :param demand: Список объемов потребностей.
    :param cost: Матрица тарифов (затрат на транспортировку).
    :return: Опорный план (матрица поставок).
    """
    # Создаем матрицу для плана поставок
    rows, cols = len(supply), len(demand)
    plan = [[0 for _ in range(cols)] for _ in range(rows)]
    used = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Копии для изменения
    supply_left = supply[:]
    demand_left = demand[:]
    
    while any(supply_left) and any(demand_left):
        # Найти минимальный тариф
        min_value = float('inf')
        min_pos = (-1, -1)
        for i in range(rows):
            for j in range(cols):
                if not used[i][j] and cost[i][j] < min_value:
                    min_value = cost[i][j]
                    min_pos = (i, j)
        
        # Найти объем поставки
        i, j = min_pos
        allocation = min(supply_left[i], demand_left[j])
        plan[i][j] = allocation
        supply_left[i] -= allocation
        demand_left[j] -= allocation
        used[i][j] = True
        
        # Если запас или спрос полностью удовлетворен, отметить ячейку как использованную
        if supply_left[i] == 0:
            for k in range(cols):
                used[i][k] = True
        if demand_left[j] == 0:
            for k in range(rows):
                used[k][j] = True
    
    return plan

def main():
    print("Метод минимальных тарифов для транспортной задачи.")
    
    # Ввод данных
    supply = list(map(int, input("Введите объемы поставок (через пробел): ").split()))
    demand = list(map(int, input("Введите объемы потребностей (через пробел): ").split()))
    
    print("Введите матрицу тарифов (через пробелы, строки разделяйте Enter):")
    cost = []
    for _ in range(len(supply)):
        cost.append(list(map(int, input().split())))
    
    # Проверка сбалансированности задачи
    if sum(supply) != sum(demand):
        print("Ошибка: задача несбалансирована. Сумма поставок должна равняться сумме потребностей.")
        input("Нажмите Enter, чтобы завершить программу.")
        return
    
    # Вывод исходной таблицы
    print("\nИсходная матрица тарифов:")
    print_matrix(cost, list(range(len(supply))), list(range(len(demand))))
    
    # Решение методом минимальных тарифов
    plan = min_tariff_method(supply, demand, cost)
    
    # Вывод результата
    print("\nОпорный план (матрица поставок):")
    print_matrix(plan, list(range(len(supply))), list(range(len(demand))))

    # Ждем ввода от пользователя, чтобы консоль не закрывалась
    input("Нажмите Enter, чтобы завершить программу.")

if __name__ == "__main__":
    main()
