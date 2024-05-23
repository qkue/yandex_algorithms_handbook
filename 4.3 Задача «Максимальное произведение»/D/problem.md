# Максимальное произведение четырех чисел

Дана последовательность целых чисел a<sub>1</sub>,…,a<sub>n</sub>​. Вычислите

max⁡<sub>1≤i≠j≠k≠l≤n</sub>a<sub>i</sub>⋅a<sub>j</sub>⋅a<sub>k</sub>⋅a<sub>l</sub>​.

Обратите внимание, что индексы i, j, k и l должны быть различны. Хотя в каких-то случаях значения элементов могут совпадать, то есть, например, a<sub>i</sub>\=a<sub>l</sub>.

## Формат ввода

Первая строка содержит целое число n. Следующая строка содержит n целых чисел a<sub>q</sub>,…,a<sub>n</sub>​ (разделены пробелами).

Ограничения: 4≤n≤2⋅10<sup>5</sup>; −2⋅10<sup>4</sup>≤a<sub>1</sub>,…,a<sub>n</sub>≤2⋅10<sup>4</sup>.

## Формат вывода

Максимальное произведение четырех элементов.

### Пример 1

Ввод

    4
    1 2 3 4
    

Вывод

    24
    

### Пример 2

Ввод

    4
    -1 -2 3 4
    

Вывод

    24
    

### Пример 3

Ввод

    5
    -1 -3 -2 -4 -5
    

Вывод

    120
    

### Пример 4

Ввод

    6
    0 -1 0 -3 -2 100
    

Вывод

    0
    

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
