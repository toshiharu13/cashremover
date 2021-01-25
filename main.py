import os

def del_old_files():
    try:
        os.remove(f'{way_to_file}dictionariesCache')
        print(f'Успешно удалено dictionariesCache на {ARM}')
    except FileNotFoundError:
        print(f'нет файла dictionariesCache {ARM}')
    try:
        os.remove(f'{way_to_file}dictionariesCacheOptimized')
        print(f'Успешно удалено dictionariesCacheOptimized на {ARM}')
    except FileNotFoundError:
        print(f'нет файла dictionariesCacheOptimized на {ARM}')

def mount(ARM):
    os.system(f'sudo mount -t cifs //{ARM}/c$ /home/boyko-ab/mnt/logs2/ --verbose -o user={login},password={password}')
    print(f'Подключились к {ARM}')

def unmount():
    print(f'Отключаемся от {ARM}')
    os.system(f'sudo umount /home/boyko-ab/mnt/logs2/')


# динамичное определение папки, где всё хранится
way_to = os.path.abspath(__file__)
way_to = os.path.dirname(way_to)

login = input('введите логин ')
password = input('введите пароль ')
way_to_file = '/home/boyko-ab/mnt/logs2/ProgramData/Protei/DispatchTerminal/'

with open(f'{way_to}/listarm.txt', 'r') as infile:
    for line in infile:
       ARM = line.strip()
       mount(ARM)
       del_old_files()
       unmount()
