# Ханойские башни

Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3. Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх. Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу. Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, только если он пустой или верхний диск на нём большего размера, чем перемещаемый. Цель головоломки — перенести все диски со стержня 1 на стержень 3.

Требуется найти последовательность ходов, которая решает головоломку <<Ханойские башни>>.

## Формат ввода

В первой строке задано одно число n (3≤n≤10) — количество дисков на первой башне.

## Формат вывода

В первой строке выведите количество операций k.

В следующих k строках выведите по два числа в каждой x<sub>i</sub>,y<sub>i</sub> (1≤x<sub>i</sub>,y<sub>i</sub>≤3) — переместить верхний диск со стержня x<sub>i</sub>​ на стержень y<sub>i</sub>​.

### Пример 1

Ввод

    3
    

Вывод

    7
    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3
    

### Пример 2

Ввод

    4
    

Вывод

    15
    1 2
    1 3
    2 3
    1 2
    3 1
    3 2
    1 2
    1 3
    2 3
    2 1
    3 1
    2 3
    1 2
    1 3
    2 3
    

### Пример 3

Ввод

    5
    

Вывод

    31
    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3
    1 2
    3 2
    3 1
    2 1
    3 2
    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3
    2 1
    3 2
    3 1
    2 1
    2 3
    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3
    


<table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256.0Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
