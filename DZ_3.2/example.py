import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def getTextFromFile(pathFrom):
    with open(pathFrom, mode='r', encoding='utf-8') as file:
        data = file.read()
    return data


def writeTextToFile(translate, pathTo):
    with open(pathTo, mode='w', encoding='utf-8') as file:
        file.write(translate)



def translate_from_file_to_file(pathFrom, pathTo, lanFrom, langTo):
    textFrom = getTextFromFile(pathFrom)
    translate = translate_it(textFrom, lanFrom, langTo)
    writeTextToFile(translate, pathTo)


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    # print(translate_it('привет', 'en'))
    file_path = 'lang\ES.txt'
    output_file_path = 'test.txt'
    translate_from_file_to_file(file_path, output_file_path, 'es', 'ru')

