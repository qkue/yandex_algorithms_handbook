# Максимальное произведение

Дана последовательность неотрицательных целых чисел a<sub>1</sub>,…,a<sub>n</sub>​. Вычислите

max⁡ a<sub>i</sub>⋅a<sub>j</sub>,1≤i≠j≤n.

Обратите внимание, что i и j должны быть разными, хотя в каких-то случаях можно наблюдать, что a<sub>i</sub>\=a<sub>j</sub>​.

## Формат ввода

Первая строка содержит целое число n. Следующая строка содержит n неотрицательных целых чисел a<sub>1</sub>,…,a<sub>n</sub>​ (разделены пробелами).

Ограничения: 2≤n≤2⋅10<sup>5</sup>; 0≤a<sub>1</sub>,…,a<sub>n</sub>≤2⋅10<sup>5</sup>.

## Формат вывода

Максимальное попарное произведение.

### Пример 1

Ввод

    3
    1 2 3
    

Вывод

    6
    

### Пример 2

Ввод

    2
    0 1
    

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
