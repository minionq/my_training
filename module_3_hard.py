
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    summ = 0
    for item in args:
        if isinstance(item, int):
            summ += item
        elif isinstance(item, str):
            summ += len(item)
        elif isinstance(item, dict):
            summ += calculate_structure_sum(*item.values(), *item.keys()) # Суммируем значения И ключи (преобразованные в строки)
        elif isinstance(item, type(None)):
            pass
        else:
            summ += calculate_structure_sum(*item)
    return summ
result1 = calculate_structure_sum(data_structure)
print(result1)
