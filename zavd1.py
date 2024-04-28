
def total_salary(path):
    total_salary = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary
                count += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None
    
    if count == 0:
        print("Файл порожній.")
        return None, None
    
    average_salary = total_salary / count
    return total_salary, average_salary

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
