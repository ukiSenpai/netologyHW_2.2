# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json
from collections import Counter
import xml.etree.ElementTree as ET

def parseDate(date) :

    counter = Counter()
    for item in date:
       counter.update(Counter(str(item).split(" ")))
    return counter

def parseCounerDate(counter):

   return [(key, val) for key, val in sorted(counter.items(), key=lambda i: i[1], reverse=True) if len(key)>6][:10]


def parseJson(path):

    with open(path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    rez = []
    for item in data['rss']["channel"]["items"]:
       rez.append(item["description"])
    return rez


def parseXml(path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser)
    root = tree.getroot()
    date = []
    for elem in root[0].findall("item"):
        date.append(elem.find("description").text)
    return date


if __name__ == '__main__':
    print(parseCounerDate(parseDate(parseJson("newsafr.json"))))
    print(parseCounerDate(parseDate(parseXml("newsafr.xml"))))

