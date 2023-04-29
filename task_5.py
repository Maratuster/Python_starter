"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def ping_site(website):
    ping_list = ['ping', website]
    console_ping = subprocess.Popen(ping_list, stdout=subprocess.PIPE)
    for line in console_ping.stdout:
        result = chardet.detect(line)
        print(line.decode(encoding=result['encoding']))
        sleep(1)

sites_list = ['gb.ru', 'github.com']

with ThreadPoolExecutor(max_workers=len(sites_list)) as executor:
    results = executor.map(ping_site, sites_list)
