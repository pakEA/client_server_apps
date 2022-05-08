"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

args = ['ping', 'yandex.ru', 'youtube.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for item in subproc_ping.stdout:
    result = chardet.detect(item)
    item = item.decode(result['encoding']).encode('utf-8')
    print(item.decode('utf-8'))
