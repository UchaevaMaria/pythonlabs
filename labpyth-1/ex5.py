import math

def safe_apply(func, data):
    results = []
    errors = []
    
    for item in data:
        try:
            result = func(item)
            results.append(result)
        except Exception as e:
            errors.append((item, e))  # сохраняем элемент и объект исключения
    
    return results, errors
#демонстрация работы функции
data = ['4', '16', 'text', '-25', '9.0']
#лямбда-функция: сначала преобразуем в float, затем вычисляем квадратный корень
func = lambda x: math.sqrt(float(x))

results, errors = safe_apply(func, data)

print("Результаты успешных вычислений:", results)
print("Ошибки:")
for element, exc in errors:
    print(f"Элемент: {element}, Ошибка: {type(exc).__name__} — {exc}")