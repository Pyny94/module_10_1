import threading
from datetime import datetime
from threading import Thread
from time import sleep




def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f"Какое-то слово № {i}\n>")
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

wite_words(10,"example1.txt")
wite_words(30,"example2.txt")
wite_words(200,"example3.txt")
wite_words(100,"example4.txt")

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа функции {time_res}')


time_start2 = datetime.now()

threads = []
threads_args = [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]
for args in threads_args:
    t = threading.Thread(target = wite_words, args = args)
    t.start()
    threads.append(t)
for t in threads:
    t.join()

time_end2 = datetime.now()
print(f"Работа потоков {time_end2 - time_start2}")
