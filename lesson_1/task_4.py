"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
words_in_bytes = []

for item in words:
    byte_item = item.encode('utf-8')
    words_in_bytes.append(byte_item)

words = []
print(words_in_bytes)

for item in words_in_bytes:
    str_item = item.decode('utf-8')
    words.append(str_item)
    
print(words)
