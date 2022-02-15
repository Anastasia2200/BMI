print ('Как вас зовут?')
name = str(input())
print ('Добрый день, ', name, ', я вычислю индекс массы вашего тела!')
print ('Сколько вам полных лет?')
age = int(input())
print ('Напишите, пожалуйста, ваш рост.')
height = float(input())
print ('Напишите ваш вес.')
weight = float(input())

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print('Ошибочные входные данные')
else:
    bmi = weight/height**2
    bmi = round(bmi, 2)
    print('Ваш индекс массы тела: ', str(bmi))
    if bmi < 18.5:
        description = ('недостаточной массой тела')
    elif 18.5 <= bmi <= 24.99:
        description = ('нормальной массой тела')
    elif 25 <= bmi <= 29.99:
        description = ('избыточной массой тела')
    else :
        description = ('ожирением')
    print('Вы относитесь к группе людей с ', description)
