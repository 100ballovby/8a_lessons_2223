num = input('Введите число: ')

num_eval = eval(num)
print(num_eval, type(num_eval))
# eval автоматически определяет тип данных и преобразовывает его
# строчки eval не воспринимает
