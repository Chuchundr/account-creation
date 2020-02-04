from openpyxl import load_workbook


class ExpressCreating:

    def __init__(self, filename):
        self.filename = filename
        self.wb = load_workbook(filename=self.filename, data_only=True)
        self.data = self.wb['Sheet1']

    def transliterate(self, name):

        slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'ye', 'ё': 'yo',
                  'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                  'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
                  'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
                  'ю': 'u', 'я': 'ya', 'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd', 'Е': 'Ye', 'Ё': 'Yo',
                  'Ж': 'j', 'З': 'z', 'И': 'i', 'Й': 'Y', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n',
                  'О': 'o', 'П': 'p', 'Р': 'r', 'С': 's', 'Т': 't', 'У': 'u', 'Ф': 'Х', 'х': 'h',
                  'Ц': 'c', 'Ч': 'Ch', 'Ш': 'sh', 'Щ': 'sh', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'e',
                  'Ю': 'u', 'Я': 'Ya',',':'','?':'',' ':'_','~':'','!':'','@':'@','#':'',
                  '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
                  ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
                  '[':'',']':'','{':'','}':''}

        for key in slovar:
            name = name.replace(key, slovar[key])
        return name


    def personal_data(self):
        people = []
        for i in self.data.values:
            person = {}
            name = i[1].split(' ')
            person['surname'] = name[0]
            person['name'] = name[1]
            try:
                person['middlename'] = f'{name[2]} {name[3]}'
            except IndexError:
                person['middlename'] = name[2]
            person['email'] = self.transliterate(f"{person['name'][0].lower()}{person['surname'].lower()}@texnomart.uz")
            people.append(person)
        return people





