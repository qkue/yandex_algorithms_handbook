# Рекламная кампания

У вас есть популярная страница в интернете, на которой есть n рекламных мест. Вы хотите продать их рекламодателям. Аналитики рассчитывают на $clicks_1​, clicks_2​, \ldots clicks_n$​ кликов в день, соответственно.

С вами связались n рекламодателей, которые готовы заплатить $price\_1$​, $price\_2​, \ldots price\_n$​ за клик.

Как подобрать пары рекламных мест и рекламодателей так, чтобы получить максимальную прибыль?

## Формат ввода

В первой строке приведено целое число n, во второй — последовательность целых чисел $price\_1, \dotsc, price\_n$ , в третьей — последовательность целых чисел $clicks\_1, \dotsc, clicks\_n$​.

Ограничения: $1 \leq n \leq 10^3$; $0 \leq price\_i, clicks\_i \leq 10^5$ для всех $1 \leq i \leq n$.

## Формат вывода

Максимальное значение $(price\_1 \cdot c\_1 + \dotsm + price\_n \cdot c\_n)$, где $c\_1, \dotsc, c\_n$ — это перестановка $clicks\_1, \dotsc, clicks\_n$​.

### Пример 1

Ввод

    1
    23
    39
    

Вывод

    897
    

### Пример 2

Ввод

    3
    2 3 9
    7 4 2
    

Вывод

    79
    

<table>
 <tr class="time-limit">
    <td class="property-title">Ограничение времени</td>
    <td>2&nbsp;секунды</td>
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
