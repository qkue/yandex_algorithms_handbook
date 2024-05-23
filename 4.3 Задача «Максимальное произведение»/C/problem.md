# Максимальное произведение трех чисел

Дана последовательность целых чисел a<sub>1</sub>,…,a<sub>n</sub>. Вычислите

max <sub>1≤i≠j,i≠k,j≠k≤n</sub> a<sub>i</sub>⋅a<sub>j</sub>⋅a<sub>k</sub>.

Обратите внимание, что индексы i, j и k должны быть различны. Хотя в каких-то случаях значения элементов могут совпадать, то есть, например, a<sub>i</sub>\=a<sub>j</sub>​.

## Формат ввода

Первая строка содержит целое число n. Следующая строка содержит n целых чисел a<sub>1</sub>,…,a<sub>n</sub> (разделены пробелами).

Ограничения: 3≤n≤2⋅10<sup>5</sup>; −2⋅10<sup>5</sup>≤a<sub>1</sub>,…,a<sub>n</sub>≤2⋅10<sup>5</sup>.

## Формат вывода

Максимальное произведение трех элементов.

### Пример 1

Ввод

    3
    1 2 3
    

Вывод

    6
    

### Пример 2

Ввод

    3
    -1 -2 -2
    

Вывод

    -4
    

### Пример 3

Ввод

    4
    -1 -3 -2 -4
    

Вывод

    -6
    

### Пример 4

Ввод

    5
    -1 0 -3 -2 0
    

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
