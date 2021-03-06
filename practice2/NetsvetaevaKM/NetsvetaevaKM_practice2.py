# coding=utf8
"""
    Дан текстовый файл, каждая строка которого содержит изображения нескольких
    чисел, разделенных пробелами (вещественные числа имеют ненулевую дробную
    часть). Создать файл вещественных чисел, содержащий (в том же порядке) все
    числа из исходного файла, имеющие ненулевую дробную часть.
        
"""

    
filename = "myFile.txt"
filename2 = "myFile2.txt"

f1 = open(filename, "r")# открываем файл для чтения
f2 = open(filename2, "w")# открываем файл для записи

for substr in f1.read().split():
    s = substr.split('.')# разбиваем все элементы по точке
    if len(s) == 2:# если число элементов равно двум
        if s[0] != '' and s[1] != '':# проверяем что оба элемента не пустые
            print s
            # проверяем, чтобы в обоих элементах были числа
            if s[1]>='0' and s[1]<='9' and s[0]>='0' and s[0]<='9':
                # если второй элемент ненулевой
                if float(s[1])!=0:
                    # запись в файл, сливаем оба элемента в вещественное число
                    f2.write("%s " % ".".join(s))
          

f1.close()
f2.close()# закрываем файлы
