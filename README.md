# Метод минимальных тарифов для решения транспортной задачи

## Краткое описание программного обеспечения

Эта программа реализует вычисление опорного плана для транспортной задачи с использованием метода минимальных тарифов. Пользователь вводит данные о поставщиках, потребителях и тарифах между ними, а программа рассчитывает оптимальный план распределения ресурсов.

## Инструкция по установке и запуску
1.Перейдите в папку dist, где находится скомпилированный файл программы.
2.Найдите файл main.exe.
3.Дважды щелкните на main.exe, чтобы запустить программу.
4.Программа не требует установки Python или других дополнительных библиотек.

## Инструкция по использованию

1.При запуске программы следуйте инструкциям на экране:
Введите объемы поставок от каждого поставщика через пробел.
Введите объемы потребностей каждого потребителя через пробел.

Введите матрицу тарифов (затрат на транспортировку) построчно, разделяя элементы пробелами.
2.Программа проверит баланс задачи:
Если сумма поставок равна сумме потребностей, программа продолжит расчет.
Если задача несбалансирована, программа сообщит об ошибке и завершит работу.

3.После ввода данных программа выведет:
Исходную матрицу тарифов.
Опорный план (матрицу поставок), рассчитанный методом минимальных тарифов.

### Пример работы программы

Пример ввода:
Введите объемы поставок: 20 30 25
Введите объемы потребностей: 10 35 20 10
Введите матрицу тарифов:
8 6 10 9
9 12 13 7
14 9 16 5
Пример вывода:
Исходная матрица тарифов:
       0    1    2    3
  0 |   8    6   10    9
  1 |   9   12   13    7
  2 |  14    9   16    5

Опорный план (матрица поставок):
       0    1    2    3
  0 |  10   10    0    0
  1 |   0   25    5    0
  2 |   0    0   15   10
После вывода результатов нажмите Enter, чтобы завершить работу программы.

## Документация

Функция min_tariff_method(supply, demand, cost):

Принимает объемы поставок, потребностей и матрицу тарифов.
Возвращает опорный план (матрицу поставок), рассчитанный методом минимальных тарифов.
Функция print_matrix(matrix, row_labels, col_labels):

Форматирует и выводит заданную матрицу (например, тарифов или поставок).
Функция main():

Организует ввод данных, проверяет их корректность и запускает расчет опорного плана.

## Инструкция по совместной работе

Если вы хотите предложить улучшения или внести изменения в код:
1.Создайте форк репозитория.
2.Переключитесь на новую ветку
git checkout -b feature-branch-name
3.Внесите изменения в код и закоммитьте их:
git commit -m "Описание изменений"
4.Отправьте изменения в свой форк:
git push origin feature-branch-name
5.Создайте Pull Request в оригинальный репозиторий.

## Информация об авторских правах и лицензировании
Данный проект доступен под лицензией MIT. Вы можете использовать, копировать, изменять и распространять код на условиях данной лицензии.

Автор: Колоколов Роман Игоревич группа: 22исп7
