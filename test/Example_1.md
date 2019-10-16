## Задание
Есть матрица `2n-1` x `2n-1`, заполненная случайными значениями. Надо вывести их на экран в ряд, начиная из центра по спирали: влево - вниз - вправо - вверх и т.д.

## Пример
Если матрица:
```
1 2 3
4 5 6
7 8 9
```
То результат:
```
5 4 7 8 9 6 3 2 1
```
Решение должно быть для общего случая с любым n, написано на Go.

## Запуск
```
$ go build
$ ./helix-matrix --help
Usage of ./helix-matrix:
  -max uint
        Max value for matrix cell (default 90)
  -n uint
        Matrix size (default 2)
$ ./helix-matrix
 41 87 47
 29 31 78
 25 80 76

31 29 25 80 76 78 47 87 41
```