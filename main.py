from app import wikicountry as wik
from app import md5iter as md5
from app import progressbar as prb
import os

def main():
    # Задача 1
    #текущая директория
    curdir=os.getcwd()

    #"""

    jsonfile=input('Введите имя json-файла с данными о странах (должен быть в текущей директории!): ')
    # проверка ввода
    if jsonfile == '':
        print('Sorry - Empty input ... .')
        return
    resfile=input('Введите имя файла с результатами: ')
    # проверка ввода
    if resfile == '':
        print('Sorry - Empty input ... .')
        return

    #оформляем полный путь
    jsonfile=os.path.join(curdir,jsonfile)
    resfile = os.path.join(curdir, resfile)

    # создаем экземмпляр класса
    wikicount=wik.Wikicountry(jsonfile,resfile)
    #загружаем страны
    wikicount.loaddata()

    # Initial call to print 0% progress
    prb.printProgressBar(0, wikicount.end, prefix='Progress:', suffix='Complete', length=50)
    # записываем результаты итерирования в файл
    print('Ищем web-страницы со странами из Wikipedia:')
    with open(wikicount.wikifile,'w') as document:
        #document.write('['+'\n')
        for i,country in enumerate(wikicount):
            #print(country)
            #print(type(country))

            if country !=None:
                # преобразовываем словарь в строку JSON
                #data=json.dumps(country)
                #json.dump(data,document,ensure_ascii=False, indent=2)
                document.write(str(country))
                document.write('\n')
        #document.write(']'+'\n')
        prb.printProgressBar(i+1, wikicount.end, prefix='Progress:', suffix='Complete', length=50)


    #"""

    #Задача 2
    file=input('Введите имя файла для построчного хэширования (должен быть в текущей директории!): ')
    # проверка ввода
    if file == '':
        print('Sorry - Empty input ... .')
        return

    # оформляем полный путь
    file = os.path.join(curdir, file)
    #итерируем файл по каждой строке, возвращаея md5 хзш
    md5iter=md5.Md5hashiter(file)
    for item in md5iter:
        print(item.hexdigest())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
