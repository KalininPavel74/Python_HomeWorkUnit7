# Калинин Павел 22.01.2023
# Знакомство с языком Python (семинары) 
# Урок 7. 
# Домашняя работа

taskName = '''Задание  №1. Создать телефонный справочник 
с возможностью импорта и экспорта данных в нескольких форматах.
           '''
menu1 = '''Импортировать данные в справочник:
1. start.csv
2. out.csv
:'''

menu2 = '''Меню:
1. отфильтровать записи по фамилии:
2. удалить запись по номеру строки:
3. добавить запись:    (каждый элемент отдельно)
4. сохранить данные в файлы out.csv, out.xml
5. выйти из программы с сохранением
6. выйти из программы без сохранения
:'''

def load_text_from_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

def save_text_to_file(file, lines):
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

print("-----------------------------------\n\r"+taskName)
phone_book = []
max_id = int(0)
a = int(input(menu1))
file = ''
if   a == 1: #
    file = 'start.csv'
    list1 = load_text_from_file(file)
    for s in list1:
        phone_book.append( s.split(';')[:3] )
    max_id = max(map(int, [list1[0] for list1 in phone_book]))        
elif a == 2: #
    file = 'out.csv'
    list1 = load_text_from_file(file)
    for s in list1:
        phone_book.append( s.split(';')[:3] )
    max_id = max(map(int, [list1[0] for list1 in phone_book]))        

#print(phone_book)
for list1 in phone_book:
    print(' '.join(list1))

while(True):
    print('')
    a = int(input(menu2))
    file = ''
    if   a == 1: # 1. отфильтровать записи по фамилии:
        search_text = input('Введите текст для поиска :')
        lines = [' '.join(list1) for list1 in phone_book if search_text in list1[1]] 
        print('')
        if len(lines):
            print('Найденные записи:')
            for list1 in lines:
                print(list1)
        else: print(f'Записи с текстом "{search_text}" не найдены.')
    elif a == 2: # 2. удалить запись по номеру строки:
        id = input('Введите номер записи для удаления:')
        for list1 in phone_book:
            if id == list1[0]:
                phone_book.remove(list1)
                print('Удалена запись:')
                print(*list1)
                break
    elif a == 3: # 3. добавить запись:    (каждый элемент отдельно)
        fio = input('Введите Ф.И.О.:')
        phone_number = input('Введите номер телефона:')
        max_id += 1
        phone_book.append([str(max_id),fio,phone_number])
    elif a == 4: # 4. сохранить данные в файлы out.csv, out.xml
        file = 'out.csv'
        lines = [';'.join(list1)+';\n' for list1 in phone_book]
        save_text_to_file(file, lines)
        print(f'Сохранено {len(lines)} записей.')
    elif a == 5: # 5. выйти из программы с сохранением
        file = 'out.csv'
        lines = [';'.join(list1)+';\n' for list1 in phone_book]
        save_text_to_file(file, lines)
        print(f'Сохранено {len(lines)} записей.')
        exit()
    elif a == 6: # 6. выйти из программы без сохранения
        exit()
