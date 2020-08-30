import json
import requests

class Wikicountry:
    def __init__(self, jsonfile, resfile):
        self.jsonfile=jsonfile
        self.wikifile=resfile
        #для десериализации JSON-файла
        self.jsondata=None
        self.start=0
        self.end=0
        self.requrl="https://ru.wikipedia.org/wiki/"

    def loaddata(self):
        with open(self.jsonfile,encoding='utf-8') as file:
            self.jsondata=json.load(file)

        #здесь проверка, что данные успешно загрузились
        # инициируем end
        self.end=len(self.jsondata)

    def __iter__(self):
        return self

    def __next__(self):
        self.start+=1
        if self.start==self.end:
            raise StopIteration
        #получаем страну
        country=self.jsondata[self.start]['name']['common']
        #проверяем на существование страницы в Wiki
        requrl=self.requrl+country
        #запрос
        response=requests.get(requrl)

        if response:
            #print(f'Success for {country}!')
            #return country
            #return {country,requrl}
            return {country:requrl}
        else:
            #print('An error has occurred.')
            return None
