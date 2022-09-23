num = input('Введите число: ')

print(type(num))
# type - определяет тип данных объекта
num_int = int(num)
num_float = float(num)
num_bool = bool(num)
print(type(num_int), num_int)
print(type(num_float), num_float)
print(type(num_bool), num_bool)
# bool даст False, только если получит 0, None, ''
