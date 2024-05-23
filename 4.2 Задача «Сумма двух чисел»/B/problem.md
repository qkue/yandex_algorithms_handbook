# A(x) + B(x)

Решите немного более сложную задачу.

Необходимо вычислить сумму двух многочленов A(x)\=a<sub>n</sub>⋅x<sup>n</sup>+…+a<sub>1</sub>⋅x+a<sub>0</sub> и B(x)\=b<sub>m</sub>⋅x<sup>m</sup>+…+b<sub>1</sub>⋅x+b<sub>0</sub>​.

## Формат ввода

В первой строке записано одно целое число n (0≤n≤10). В второй строке записаны числа a<sub>n</sub>,a<sub>n-1</sub>,…,a<sub>0</sub> (−100≤a<sub>i</sub>≤100, a<sub>n</sub>≠0).

В третьей строке записано одно целое число m (0≤m≤10). В четвертой строке записаны числа b<sub>m</sub>,b<sub>m-1</sub>,…,b<sub>0</sub> (−100≤b<sub>i</sub>≤100, b<sub>m</sub>≠0).

Гарантируется, что a<sub>n</sub>+b<sub>m</sub>≠0.

## Формат вывода

В первой строке выведите число k — степень многочлена A(<i>x</i>)+B(<i>x</i>).

В второй строке выведите коэффициенты этого многочлена: c<sub>k</sub>,c<sub>k-1</sub>,…,c<sub>1</sub>,c<sub>0</sub>​.

### Пример 1

Ввод

    3
    1 2 3 4
    2
    1 0 0
    

Вывод

    3
    1 3 3 4 
    

### Пример 2

Ввод

    0
    1
    9
    1 2 3 4 5 6 7 8 9 0
    

Вывод

    9
    1 2 3 4 5 6 7 8 9 1 
    

### Пример 3

Ввод

    1
    1 1
    1
    1 1
    

Вывод

    1
    2 2 
    


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
