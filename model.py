# Модуль данных телефонного справочника

FIELD_NUM_ID = 0 # поле ИД
FIELD_NUM_FIO = 1 # поле Ф.И.О.
FIELD_NUM_PNS = 2 # поле номера телефонов

FIELD_RUS_NAME_ID  = '№' # поле ИД
FIELD_RUS_NAME_FIO = 'Ф.И.О.' # поле Ф.И.О.
FIELD_RUS_NAME_PNS = 'Номера телефонов' # поле номера телефонов

FIELD_LAT_NAME_ID  = 'order_number' # поле ИД
FIELD_LAT_NAME_FIO = 'fio' # поле Ф.И.О.
FIELD_LAT_NAME_PNS = 'phone_numbers' # поле номера телефонов

DB_RUS_NAME = 'Телефонный справочник'
DB_LAT_NAME = 'phone_book'
FIELD_LAT_NAME_PN = 'phone_number' # ном. тел. в поле номера телефонов
RECORD_LAT_NAME = 'record' # обозначение одной записи в справочнике

FIELDS_LIST_RUS_NAME = [FIELD_RUS_NAME_ID, FIELD_RUS_NAME_FIO, FIELD_RUS_NAME_PNS]
FIELDS_LIST_LAT_NAME = [FIELD_LAT_NAME_ID, FIELD_LAT_NAME_FIO, FIELD_LAT_NAME_PNS]
QTY_FIELDS = len(FIELDS_LIST_RUS_NAME) # кол-во поей в телефонном справочнике

# Хранилище записей телефонного справочника
phone_book = []
# Максимальный номер записи (не уменьшается при удалении последней записи)
max_id = int(0)

# для всех других модулей телефонный справочник - это список состояций из списков
def get_DB_as_list_of_lists():
    return phone_book

def get_next_id():
    return max_id+1

def init_max_id():
    global max_id
    max_id = max(map(int, [lst[FIELD_NUM_ID] for lst in phone_book]))

def init(lst):
    for s in lst:
        phone_book.append(s)
    init_max_id()

def get_found_lists(search_text):
    lst = []
    for list1 in phone_book:
        for s in list1[1:]:
            if search_text in s:
                lst.append(list1)
                break
    return lst

def delete_by_id(id: int):
    for lst in phone_book:
        if str(id) == lst[FIELD_NUM_ID]:
            phone_book.remove(lst)
            return lst
    return None    

def add_record(fields):
    global max_id
    max_id += 1
    lst = [str(max_id),*fields]
    phone_book.append(lst)
    return lst

def update_by_id(id: int, fields):
    for i, lst in enumerate(phone_book):
        if str(id) == lst[FIELD_NUM_ID]:
            lst = [str(id), *fields]
            phone_book[i] = lst
            return lst
    return None    

