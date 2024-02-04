# подключаем из библиотеки itertools функцию product
from itertools import product

def count_codes():
    letters = ['И', 'В', 'А', 'Н']
    count = 0 # создаем счетчик 
    
    for code in product(letters, repeat=5): # создаем комбинации из 5 возможных букв
        if code.count('И') >= 1: 
            count += 1 # проверяем сколько комбинаций содержат 1 букву 'И' и считаем только их
    
    return count #возвращаем счетчик(функцию)

print(count_codes()) 
