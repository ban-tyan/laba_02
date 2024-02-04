# laba_02
## Вариант 10
>**Условие 1**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/d2a40286-86cd-42db-898e-64f43948b0a1)
```pytnon
# 1. подключаем из библиотеки itertools функцию product
from itertools import product

def count_codes():
    letters = ['И', 'В', 'А', 'Н']
    count = 0 # создаем счетчик 
    
    for code in product(letters, repeat=5): # создаем комбинации из 5 возможных букв
        if code.count('И') >= 1: 
            count += 1 # проверяем сколько комбинаций содержат 1 букву 'И' и считаем только их
    
    return count #возвращаем счетчик(функцию)

print(count_codes()) 

>**Условие 2**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/6398be88-ebdd-432a-b9ec-e7a07dbbd795)

>**Условие 3**
>![image](https://github.com/ban-tyan/laba_02/assets/145260845/bff5c071-3b9f-4c5d-893e-c59416899a62)
