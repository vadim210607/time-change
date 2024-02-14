import os
import json
from datetime import datetime

# Шлях до папки, де знаходяться файли
folder_path = "F:\999 backup\PHOTO\Vadim\Photos from 2004"
trash_json = []


def change_time():

    count_done, count_exc = 0, 0

    # Ітеруємося по файлам у папці
    for filename in os.listdir(folder_path):

        # Перемінна шляху кожного JSON
        json_file_path = os.path.join(folder_path, filename)

        # Перевірка, чи файл є JSON-файлом
        if filename.endswith(".json") and os.path.isfile(json_file_path) and filename != "метадані.json":
            try:

                # Відкриваємо JSON-файл і зчитуємо дані
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)

                    # Отримуємо дані зі словника за ключами
                    title = data["title"]
                    timestamp = int(data["photoTakenTime"]["timestamp"])

                    # Перемінна шляху кожного JPG
                    jpg_file_path = os.path.join(folder_path, title)

                    try:

                        # Конвертуємо timestamp у формат datetime
                        datetime_obj = datetime.fromtimestamp(timestamp)

                        # Змінюємо дату створення та дату зміни у файлі
                        os.utime(jpg_file_path, (datetime_obj.timestamp(), datetime_obj.timestamp()))

                        print(f"Успішно змінено дату файлу {title} на {timestamp}")

                        count_done += 1

                        trash_json.append(filename)

                    except Exception as e:
                        print(f"Помилка зміни дати у {title}: {e}")

                        count_exc += 1

                    print("------------"*4)



            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filename}: {e}")

    # Видалення відпрацюваних JSON
    for file in trash_json:
        jpg_file = os.path.join(folder_path, file)
        os.remove(jpg_file)
        print(f'Файл {file} видалено успішно')
    print('========='*9)
    print('Програму завершено успішно!')
    print(f'Всього оброблено файлів: {count_done + count_exc}')
    print('=========' * 9)
    print(f'Успішно змінено дату у файлах: {count_done}')
    print(f'Помилки зміни дати у файлах: {count_exc}')
    print('=========' * 9)



if __name__ == '__main__':
    change_time()
