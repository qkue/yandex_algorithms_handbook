# A+B строки

Необходимо вычислить "кривую" сумму двух строк A и B одинаковой длины.

"Кривой" суммой двух строк называется операция следующего вида:

C=A+B=A<sub>1</sub>B<sub>1</sub>A<sub>2</sub>B<sub>2</sub>…A<sub>n-1</sub>B<sub>n-1</sub>A<sub>n</sub>B<sub>n</sub>​

Где n -- длина строк A и B.

## Формат ввода

В первой строке записано целое число n (1≤n≤10).

Вторая строка содержит строку A. (A<sub>i</sub>∈{a,b,…,z}).

Третья строка содержит строку B. (B<sub>i</sub>∈{a,b,…,z}).

## Формат вывода

Выведите одну строку, содержащую строку С=A+B.

### Пример 1

Ввод

    3
    abc
    def
    

Вывод

    adbecf
    

### Пример 2

Ввод

    5
    abaca
    bdaef
    

Вывод

    abbdaaceaf
    

### Пример 3

Ввод

    1
    y
    z
    

Вывод

    yz
    


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
