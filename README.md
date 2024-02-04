# laba_02
## Вариант 10
**Условие**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/d2a40286-86cd-42db-898e-64f43948b0a1)
### **Задача 1.Алгоритм**
1. подключаем из библиотеки itertools функцию product
2. объявляем функцию `def count_codes()`, в ней сначала объявляем используемые буквы и счетчик
3. в цикле for с помощью метода product()` будут создаваться комбинации
4. вводим условие на содержание хотя бы одной буквы "И", увеличиваем счетчик при выполнении условия
5. функция будет возвращать значение счетчика `count`
6. выводим на экран функцию(результат ее работы)
______

**Условие**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/6398be88-ebdd-432a-b9ec-e7a07dbbd795)
### **Задача 2.Алгоритм**
1. создаем функцию `def count_null()`
2. сохраняем выражение из задания в переменную `a`
3. переводим значение в 8-ричную систему счисления с помощью функции `oct()`. результатом будет строка, начинающаяся с префикса "0o", поэтому с помощью среза `[2:]` удаляем этот префикс
4. объявляем счетчик `count`
5. подсчитываем кол-во "0" в записи с помощью `.count`
6. функция будет возвращать значение счетчика `count`
7. выводим на экран функцию(результат ее работы)
_________

**Условие**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/bff5c071-3b9f-4c5d-893e-c59416899a62)
### **Задача 3.Алгоритм**
1. создаем функцию def find_number_with_max_delit()
2. переменная `colvo_delit` инициализируется нулем, а переменная `number_with_max_delit` - значением `None`.они используются для хранения информации о числе с максимальным количеством делителей и самом большом количестве делителей, соответственно
3. в цикле for перебираются все числа в заданном диапазоне. для каждого числа создается пустой список `deliteli`, в который будут добавляться все делители числа
4. во вложенном цикле for перебираются все числа от 1 до текущего числа (включительно). Если текущее число делится на это число без остатка, то оно добавляется в список `deliteli`
5. после завершения вложенного цикла проверяется, является ли количество делителей текущего числа больше, чем текущее максимальное количество делителей. если да, то обновляются значения `colvo_delit` и `number_with_max_delit` соответствующими значениями текущего числа и количества делителей
6. функция возвращается количество делителей и число, у которого это количество делителей достигается `colvo_delit`, `number_with_max_delit`
7. выводим на экран функцию(результат ее работы)
_________
### Результаты 
1. ![image](https://github.com/ban-tyan/laba_02/assets/145260845/98b383aa-96e7-497d-9dfe-f360377ba1a9)
2. ![image](https://github.com/ban-tyan/laba_02/assets/145260845/2f8cebf9-b95e-4726-857b-b339ceb60c96)
3. ![image](https://github.com/ban-tyan/laba_02/assets/145260845/89188d04-06c2-46ce-927a-b7035c35e096)





