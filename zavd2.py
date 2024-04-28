

def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None
    
    return cats_info

cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    print(cats_info)

